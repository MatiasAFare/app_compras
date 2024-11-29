from django.db import models
from datetime import datetime
# No utilizamos models.py porque la base de dato es no relacional
# Modelo de productos y sus atributos:

class Productos (models.Model):
    productoId = int
    product_name =  str
    price = int
    establishment_name = str
    marca =  str
    datetime = datetime
    comments = str
    images = "" #binData



