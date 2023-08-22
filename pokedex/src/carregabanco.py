import requests
from pymongo import MongoClient

# Configuração do MongoDB
mongo_client = MongoClient("mongodb://root:example@localhost:27017/")
db = mongo_client["mydatabase"]
collection = db["mycollection"]

# URL da API para obter informações (substitua pela URL real)
api_url = "https://beta.pokeapi.co/graphql/v1beta"

try:
    # Faz a solicitação à API
    for i in range (0,1008):
        response = requests.get(f"{api_url}/i")
        data = response.json()

        # Inserir os dados na coleção do MongoDB
        inserted_ids = collection.insert_many(data)

        print(f"Loaded {len(inserted_ids.inserted_ids)} records into MongoDB")
except Exception as e:
    print(f"Error: {e}")
