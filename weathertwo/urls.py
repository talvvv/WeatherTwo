from django.urls import path
from weathertwo import views

urlpatterns = [
    path("", views.home, name="home"),
]