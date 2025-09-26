import streamlit as st
import pandas as pd
from db_sqlite import init_sqlite, insert_city, list_cities, get_city_by_id
from db_mongo import init_mongo, insert_location, find_locations_by_city, find_locations_within_radius
from geoprocessamento import distance_km

init_sqlite()
init_mongo()

st.set_page_config(page_title='Persistência Poliglota', layout='wide')
st.title('Persistência Poliglota (SQLite + MongoDB)')

menu = st.sidebar.selectbox("Menu", ["Cadastrar cidade", "Cadastrar local", "Consultar"])

if menu == "Cadastrar cidade":
    st.header("Cadastrar Cidade")
    with st.form("form_city"):
        nome = st.text_input("Cidade")
        estado = st.text_input("Estado")
        pais = st.text_input("País", value="Brasil")
        submitted = st.form_submit_button("Salvar")
        if submitted:
            insert_city(nome, estado, pais)
            st.success("Cidade cadastrada!")

elif menu == "Cadastrar local":
    st.header("Cadastrar Local")
    cidades = list_cities()
    if not cidades:
        st.warning("Cadastre uma cidade primeiro!")
    else:
        with st.form("form_local"):
            nome = st.text_input("Nome do local")
            cid = st.selectbox("Cidade", cidades, format_func=lambda c: f"{c[1]} - {c[2]}")
            descricao = st.text_area("Descrição")
            lat = st.number_input("Latitude", format="%.6f")
            lon = st.number_input("Longitude", format="%.6f")
            submitted = st.form_submit_button("Salvar Local")
            if submitted:
                insert_location(nome, cid[1], {"latitude": lat, "longitude": lon}, descricao)
                st.success("Local cadastrado no MongoDB!")

elif menu == "Consultar":
    st.header("Consultar Locais")
    cidades = list_cities()
    if not cidades:
        st.warning("Nenhuma cidade cadastrada")
    else:
        cid = st.selectbox("Cidade", cidades, format_func=lambda c: f"{c[1]} - {c[2]}")
        locais = find_locations_by_city(cid[1])
        if locais:
            df = pd.DataFrame([{
                "Nome": l["nome_local"],
                "Descrição": l.get("descricao", ""),
                "Lat": l["coordenadas"]["latitude"],
                "Lon": l["coordenadas"]["longitude"]
            } for l in locais])
            st.dataframe(df)
            st.map(df.rename(columns={"Lat": "lat", "Lon": "lon"})[["lat", "lon"]])

        st.subheader("Busca por proximidade")
        lat0 = st.number_input("Latitude de referência", format="%.6f")
        lon0 = st.number_input("Longitude de referência", format="%.6f")
        raio = st.number_input("Raio (km)", value=10.0)
        if st.button("Buscar"):
            results = find_locations_within_radius((lat0, lon0), raio)
            if results:
                df2 = pd.DataFrame([{
                    "Nome": r["nome_local"],
                    "Descrição": r.get("descricao", ""),
                    "Lat": r["coordenadas"]["latitude"],
                    "Lon": r["coordenadas"]["longitude"],
                    "Distância (km)": round(distance_km((lat0, lon0), (r["coordenadas"]["latitude"], r["coordenadas"]["longitude"])), 2)
                } for r in results])
                st.dataframe(df2)
                st.map(df2.rename(columns={"Lat": "lat", "Lon": "lon"})[["lat", "lon"]])
            else:
                st.info("Nenhum local encontrado nesse raio")

