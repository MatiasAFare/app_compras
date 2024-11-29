from mongodb import *
from datetime import datetime
from bson.binary import Binary

# def add_collection(collection_name):
#     if collection_name not in db.list_collections():
#         db.create_collection(collection_name)
#         return f"Collection {collection_name} created successfully."
#     else:
#         return f"Collection {collection_name} already exists."

def add_product(product):
    required_fields = ["product_name", "price", "establishment_name", "marca", "datetime"]
    for field in required_fields:
        if field not in product:
            print(f"Error: The {field} field is mandatory and it's missing.")
            return

    if productos_collection.find_one({"productoId": product.get("productoId")}):
        print(f"Error: The ID product {product['productoId']} already exist.")
        return

    try:
        result = productos_collection.insert_one(product)
        print(f"ID created product: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred creating the product: {e}")



# ENTRA JUAN CARLO'!

def modify_product(productoId, product_name=None, price=None, establishment_name=None, brand=None, datetime=None, comments=None, images=None):
    """
    Modifica los campos del producto en la colección 'productos' en MongoDB.

    Args:
        productoId (int): El ID del producto a modificar.
        product_name (str, optional): Nombre del producto.
        price (float, optional): Precio del producto.
        establishment_name (str, optional): Nombre del establecimiento.
        brand (str, optional): Marca del producto.
        datetime (str, optional): Fecha y hora del producto.
        comments (str, optional): Comentarios sobre el producto.
        images (str, optional): URL o base64 de la imagen del producto.
    """

    # Creamos un diccionario con los campos a actualizar
    updated_fields = {}

    if product_name is not None:
        updated_fields["product_name"] = product_name
    if price is not None:
        updated_fields["price"] = price
    if establishment_name is not None:
        updated_fields["establishment_name"] = establishment_name
    if brand is not None:
        updated_fields["marca"] = brand
    if datetime is not None:
        updated_fields["datetime"] = datetime
    if comments is not None:
        updated_fields["comments"] = comments
    if images is not None:
        updated_fields["images"] = images

    # Si no se proporcionaron datos para actualizar, devolvemos un error
    if not updated_fields:
        return {"error": "No se proporcionaron datos para actualizar el producto."}

    # Realizamos la actualización en la base de datos
    result = productos_collection.update_one(
        {"productoId": productoId},  # Buscar por ID
        {"$set": updated_fields}      # Actualizar con los nuevos datos
    )

    if result.matched_count > 0:
        return {"message": "Producto modificado exitosamente."}
    else:
        return {"error": "Producto no encontrado."}