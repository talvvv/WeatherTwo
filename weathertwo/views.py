from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def basic_print(request, location):
    location = input("Enter the city:")
    unit = "metric"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=2ee40ecb425f72c75ed3612e15cbd107&units=" + unit

    
    
    