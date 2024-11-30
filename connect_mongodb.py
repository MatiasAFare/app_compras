from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('MONGODB_URL')
client = MongoClient(os.getenv("DATABASE_URL"))
db = client[os.getenv("DATABASE_NAME")]
productos_collection = db["productos"]


# print(db.list_collection_names())