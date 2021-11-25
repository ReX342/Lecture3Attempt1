from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.watch, name="watch"),
    path("create", views.create_entry, name="create"),
    path("random", views.random, name="random"),
    path("add", views.add, name="add"),
]
