from pymongo import MongoClient
from geopy.distance import geodesic

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "projeto"
COLLECTION = "locais"
_client = None

def init_mongo():
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URI)

def insert_location(nome, cidade, coordenadas, descricao=""):
    db = _client[DB_NAME]
    coll = db[COLLECTION]
    doc = {
        "nome_local": nome,
        "cidade": cidade,
        "coordenadas": coordenadas,
        "descricao": descricao
    }
    coll.insert_one(doc)

def find_locations_by_city(cidade):
    db = _client[DB_NAME]
    coll = db[COLLECTION]
    return list(coll.find({"cidade": cidade}))

def find_locations_within_radius(ponto, raio_km):
    db = _client[DB_NAME]
    coll = db[COLLECTION]
    locais = list(coll.find({}))
    results = []
    for l in locais:
        lat = l["coordenadas"]["latitude"]
        lon = l["coordenadas"]["longitude"]
        dist = geodesic(ponto, (lat, lon)).km
        if dist <= raio_km:
            results.append(l)
    return results
