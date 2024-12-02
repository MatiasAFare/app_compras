import json
from datetime import datetime
from shopilite_app.utils import parse_json
from bson import ObjectId
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from connect_mongodb import *


def index(request):
    return HttpResponse("Welcome to Shopilite App.")


@require_http_methods(["POST"])
def add_product(request):
    try:
        product_data = json.loads(request.body)
        if "datetime" in product_data:
            product_data["datetime"] = datetime.fromisoformat(
                product_data["datetime"].replace("Z", "+00:00")
            )
        products_collection.insert_one(product_data)
        return JsonResponse(parse_json(product_data))
    except Exception as error:
        return JsonResponse(parse_json(error.__dict__), status=500)


@require_http_methods(["GET"])
def count_products(request):
    count = products_collection.count_documents({})
    response_data = dict(Count=count)
    return JsonResponse(response_data)


@require_http_methods(["GET"])
def get_products(request):
    try:
        documents = parse_json(products_collection.find({}))
        return JsonResponse(documents, safe=False)
    except Exception as error:
        return JsonResponse(
            {"error": "Failed to retrieve products", "message": str(error)}, status=500
        )


@require_http_methods(["PUT"])
def modify_product(request, product_id):
    product_data = json.loads(request.body)
    product = products_collection.find_one_and_update(
        {"_id": ObjectId(product_id)}, {"$set": product_data}, return_document=True
    )
    return JsonResponse(parse_json(product))


@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    return HttpResponse(products_collection.delete_one({"_id": ObjectId(product_id)}))


@require_http_methods(["GET"])
def get_product_by_id(request, product_id):
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return JsonResponse(parse_json(product))
    else:
        return JsonResponse({"error": "Product not found."}, status=404)
