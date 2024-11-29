from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("db_test/", views.db_test, name="db_test"),
    path("db_test_dos/", views.db_test_dos, name="db_test_dos"),
    ]

