import os
from pymongo import MongoClient
from dotenv import load_dotenv
from shopilite_app.schemas import product


load_dotenv()

DB_URL = os.getenv("MONGODB_URL")
client = MongoClient(os.getenv("DATABASE_URL"))
db = client[os.getenv("DATABASE_NAME")]

if "products" in db.list_collection_names():
    print("Collection already exists")
else:
    products_collection = db.create_collection("products", validator=product)

products_collection = db["products"]
