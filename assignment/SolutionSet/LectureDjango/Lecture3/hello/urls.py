from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian),
    path("david", views.david),
    path("<str:name>", views.greet)
]