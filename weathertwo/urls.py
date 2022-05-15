from django.urls import path
from weathertwo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("weathertwo/<name>", views.basic_print, name="basic_print"),
]