from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("count_products/", views.count_products, name="count_products"),
    path("get_products/", views.get_products, name="get_products"),
]
