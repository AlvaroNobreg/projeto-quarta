# projeto-sexta
Projeto Persistência Poliglota (SQLite + MongoDB)

Este projeto demonstra o uso de persistência poliglota, integrando dois bancos de dados diferentes:

SQLite → armazenamento relacional de cidades (nome, estado, país).

MongoDB → armazenamento de locais com coordenadas geográficas (latitude/longitude).

A aplicação possui interface em Streamlit, permitindo:
✅ Cadastrar cidades (no SQLite).
✅ Cadastrar locais associados a uma cidade (no MongoDB).
✅ Listar locais por cidade.
✅ Consultar locais próximos a uma coordenada (busca por raio geográfico).

🚀 Tecnologias utilizadas

Python 3.10+

SQLite (banco relacional)

MongoDB (banco de documentos)

Streamlit (interface web)

Pandas + Geopy (processamento e cálculos de distância)


⚙️ Como rodar localmente

Clonar o repositório

git clone https://github.com/SEU_USUARIO/projeto-persistencia-poliglota.git
cd projeto-persistencia-poliglota


Criar ambiente virtual

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows


Instalar dependências

pip install -r requirements.txt


Rodar o Streamlit

streamlit run app.py


Acesse no navegador: http://localhost:8501

📊 Estrutura do projeto
projeto-persistencia-poliglota/
│── app.py                 # Interface principal Streamlit
│── db_sqlite.py           # Funções para SQLite
│── db_mongo.py            # Funções para MongoDB
│── geoprocessamento.py    # Funções de cálculo geográfico
│── requirements.txt       # Dependências
│── README.md              # Documentação
│── .gitignore             # Arquivos a ignorar no Git


💡 Possíveis melhorias

Adicionar mapas mais avançados (Folium/Leaflet).

Criar API REST para integração com outros sistemas.

Implementar índices geoespaciais no MongoDB para consultas mais rápidas.

