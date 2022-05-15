from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from django import forms
import requests

# Create your views here.

class LocationForm(forms.Form):
        location = forms.CharField(label='location', max_length=100)

def home(request):
    return HttpResponse("Hello, Django!")

def basic_print(request):
    if request.method == 'POST':
        
        form = LocationForm(request.POST)
        #print(form.as_p())
        if form.is_valid():
            location = form.cleaned_data['location']
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
                    'temperature': temperature,
                    'description' : description,
                    'humidity' : humidity,
                    'wind_speed' : wind_speed,
                    'date_time' : date_time      
                }
            )

    else:
        form = LocationForm()

    return render(request, 'weathertwo/mainpage.html', {'form': form})

    
