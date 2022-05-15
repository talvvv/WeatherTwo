from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import requests

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def basic_print(request, location):
    location = input("Enter the city:")
    unit = "metric"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=2ee40ecb425f72c75ed3612e15cbd107&units=" + unit

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        print("Invalid city")
    else:
        temperature = api_data['main']['temp']
        description = api_data['weather'][0]['description'] 
        humidity = api_data['main']['humidity'] 
        wind_speed = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")      
    
    return render(
        request,
        'weathertwo/mainpage.html',
        {
            'location': location,
            'temperature': temperature
        }
    )
