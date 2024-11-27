from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def index(request):
    return HttpResponse("Welcome to Shopilite App.")


def about(request):
    return JsonResponse({
        "lucas"
        : "cometravas",
        "goldental"
        : "comegatos"

    })