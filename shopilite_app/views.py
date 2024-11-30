from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mongodb import *

# Create your views here.


def index(request):
    return HttpResponse("Welcome to Shopilite App.")


def about(request):
    return JsonResponse({"lucas": "cometravas", "goldental": "comegatos"})


def db_test(request):
    return HttpResponse(productos_collection.count_documents({}))


def db_test_dos(request):
    return HttpResponse(db.list_collections())
