from pymongo import MongoClient
import os
from dotenv import load_dotenv
from shopilite_app.schemas import producto


load_dotenv()

DB_URL = os.getenv('MONGODB_URL')
client = MongoClient(os.getenv("DATABASE_URL"))
db = client[os.getenv("DATABASE_NAME")]

if 'productos' in db.list_collection_names():
    print("Collection already exists")
else:
    productos_collection = db.create_collection("productos", validator = producto)

productos_collection = db["productos"]
