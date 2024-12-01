import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from connect_mongodb import *



def index(request):
    return HttpResponse("Welcome to Shopilite App.")



@require_http_methods(["POST"])
def add_product(request):
        # Procesar el cuerpo del POST
        body_unicode = request.body.decode('utf-8')
        print("Contenido del POST:", body_unicode)
        return JsonResponse({"message": "Método POST recibido correctamente"})


def count_products(request):
    count = productos_collection.count_documents({})
    response_data = dict(Cantidad=count)
    return JsonResponse(response_data)


def get_products(request):
     JsonResponse(productos_collection.find({}))

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




