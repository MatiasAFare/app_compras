from connect_mongodb import db

# def add_collection(collection_name):
#     if collection_name not in db.list_collections():
#         db.create_collection(collection_name)
#         return f"Collection {collection_name} created successfully."
#     else:
#         return f"Collection {collection_name} already exists."
#
# add_collection("testJson")


def envio_json():
    json_data = {
        "test": "Primer test",
        "descripcion": "Volando solo",
        "resultado": "Si llega lucas es un gorreado"
    }

    collection = db["testJson"]
    collection.insert_one(json_data)

    print("Te la mande a guardar con exito")

if __name__ == "__main__":
    envio_json()
