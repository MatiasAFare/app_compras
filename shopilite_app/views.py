from datetime import datetime
import json
from logging import exception

from bson import ObjectId
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from bson.json_util import dumps
from connect_mongodb import *
from pymongo.errors import BulkWriteError


def index(request):
    return HttpResponse("Welcome to Shopilite App.")


@require_http_methods(["POST"])
def add_product(request):
    try:
        product_data = json.loads(request.body)
        if 'datetime' in product_data:
            product_data['datetime'] = datetime.fromisoformat(product_data['datetime'].replace("Z", "+00:00"))
        product_id = productos_collection.insert_one(product_data).inserted_id

    except Exception as error:
        # Capturar cualquier otro tipo de error
        return JsonResponse({'error': 'Unknown error', 'message': str(error)}, status=500)

    product_data['_id'] = str(product_id)
    return JsonResponse(product_data)


@require_http_methods(["GET"])
def count_products(request):
    count = productos_collection.count_documents({})
    response_data = dict(Cantidad=count)
    return JsonResponse(response_data)


@require_http_methods(["GET"])
def get_products(request):
    def serialize_document(document):
        document['_id'] = str(document['_id'])
        return document

    try:
        documents = list(productos_collection.find({}))
        serialized_documents = [serialize_document(doc) for doc in documents]
        return JsonResponse(serialized_documents, safe=False)

    except Exception as error:
        return JsonResponse({'error': 'Failed to retrieve products', 'message': str(error)}, status=500)


@require_http_methods(["PUT"])
def modify_product(request, product_id):
    product_data = json.loads(request.body)
    product = productos_collection.find_one_and_update({"_id": ObjectId(product_id)},
                                                       {"$set": {product_data}})
    print(product)
    product['_id'] = str(product['_id'])
    return JsonResponse(product)


@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    return HttpResponse(productos_collection.delete_one({"_id": ObjectId(product_id)}))


def get_product_by_id(request, product_id):
    product = productos_collection.find_one({"_id": ObjectId(product_id)})
    print(product)
    product['_id'] = str(product['_id'])
    if product:
        return JsonResponse(product)
    else:
        return JsonResponse({"error": "Product not found."}, status=404)
