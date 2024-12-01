from django.http import HttpResponse, JsonResponse
from connect_mongodb import *


# Create your views here.


def index(request):
    return HttpResponse("Welcome to Shopilite App.")


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
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({"error": {e}}, status=500)


def count_products(request):
    return JsonResponse(productos_collection.count_documents({}))

def get_products(request):
    return JsonResponse(productos_collection.find({}))

def modify_product(request, product_id):
    return JsonResponse(productos_collection.update_one({"id": product_id}))

def delete_product(request, product_id):
    return JsonResponse(productos_collection.delete_one({"id": product_id}))

def get_product_by_id(request, product_id):
    product = productos_collection.find_one({"id": product_id})
    if product:
        return JsonResponse(product)
    else:
        return JsonResponse({"error": "Product not found."}, status=404)




