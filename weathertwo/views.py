from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from django import forms
import requests
import json

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

            api_link=requests.get('https://www.metaweather.com/api/location/search/?query=' + location).text
            api_data=json.loads(api_link)
            api_location = api_data[0]['woeid']
            api_link=requests.get('https://www.metaweather.com/api/location/' + str(api_location)).text
            api_data=json.loads(api_link)
            # api_link = requests.get(complete_api_link)
            # api_data = api_link.json()

            if True:
                temperature = list()
                description = list()
                humidity = list()
                wind_speed = list()
                for i in range(4):
                    temperature.append(round(api_data['consolidated_weather'][i]['the_temp']))
                    description.append(api_data['consolidated_weather'][i]['weather_state_name']) 
                    humidity.append(api_data['consolidated_weather'][i]['humidity'])
                    wind_speed.append(api_data['consolidated_weather'][i]['wind_speed'] / 2,237)
            
            return render(
                request,
                'weathertwo/index.html',
                {
                    'location': location,
                    'temperature': temperature,
                    'description' : description,
                    'humidity' : humidity,
                    'wind_speed' : wind_speed, 
                }
            )

    else:
        form = LocationForm()

    return render(request, 'weathertwo/index.html', {'form': form})

    
