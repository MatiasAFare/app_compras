from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("count_products", views.count_products, name="count_products"),
    path("get_products", views.get_products, name="get_products"),
    path("add_product", views.add_product, name="add_product"),
    path("modify_product/<str:product_id>", views.modify_product, name="modify_product"),
    path("delete_product/<str:product_id>", views.delete_product, name="delete_product"),
    path("get_product/<str:product_id>", views.get_product_by_id, name="get_product_by_id"),

]
