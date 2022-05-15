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

                temperature1 = (round(api_data['consolidated_weather'][0]['the_temp']))
                description1 = (api_data['consolidated_weather'][0]['weather_state_name']) 
                humidity1 = (api_data['consolidated_weather'][0]['humidity'])
                wind_speed1 = (round(api_data['consolidated_weather'][0]['wind_speed'] / 2.237))
                if description1 == 'Snow':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/sn.ico'
                elif description1 == 'Sleet':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/sl.ico'
                elif description1 == 'Hail':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/h.ico'
                elif description1 == 'Thunderstorm':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/t.ico'
                elif description1 == 'Heavy Rain':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/hr.ico'
                elif description1 == 'Light Rain':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/lr.ico'
                elif description1 == 'Showers':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/s.ico'
                elif description1 == 'Heavy Cloud':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/ht.ico'
                elif description1 == 'Light Cloud':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/lc.ico'
                elif description1 == 'Clear':
                    url1 = 'https://www.metaweather.com/static/img/weather/ico/c.ico'

                temperature2 = (round(api_data['consolidated_weather'][1]['the_temp']))
                description2 = (api_data['consolidated_weather'][1]['weather_state_name']) 
                humidity2 = (api_data['consolidated_weather'][1]['humidity'])
                wind_speed2 = (round(api_data['consolidated_weather'][1]['wind_speed'] / 2.237))
                if description2 == 'Snow':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/sn.ico'
                elif description2 == 'Sleet':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/sl.ico'
                elif description2 == 'Hail':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/h.ico'
                elif description2 == 'Thunderstorm':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/t.ico'
                elif description2 == 'Heavy Rain':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/hr.ico'
                elif description2 == 'Light Rain':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/lr.ico'
                elif description2 == 'Showers':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/s.ico'
                elif description2 == 'Heavy Cloud':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/hc.ico'
                elif description2 == 'Light Cloud':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/lc.ico'
                elif description2 == 'Clear':
                    url2 = 'https://www.metaweather.com/static/img/weather/ico/c.ico'

                

                temperature3 = (round(api_data['consolidated_weather'][2]['the_temp']))
                description3 = (api_data['consolidated_weather'][2]['weather_state_name']) 
                humidity3 = (api_data['consolidated_weather'][2]['humidity'])
                wind_speed3 = (round(api_data['consolidated_weather'][2]['wind_speed'] / 2.237))
                if description3 == 'Snow':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/sn.ico'
                elif description3 == 'Sleet':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/sl.ico'
                elif description3 == 'Hail':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/h.ico'
                elif description3 == 'Thunderstorm':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/t.ico'
                elif description3 == 'Heavy Rain':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/hr.ico'
                elif description3 == 'Light Rain':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/lr.ico'
                elif description3 == 'Showers':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/s.ico'
                elif description3 == 'Heavy Cloud':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/hc.ico'
                elif description3 == 'Light Cloud':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/lc.ico'
                elif description3 == 'Clear':
                    url3 = 'https://www.metaweather.com/static/img/weather/ico/c.ico'

                temperature4 = (round(api_data['consolidated_weather'][3]['the_temp']))
                description4 = (api_data['consolidated_weather'][3]['weather_state_name']) 
                humidity4 = (api_data['consolidated_weather'][3]['humidity'])
                wind_speed4 = (round(api_data['consolidated_weather'][3]['wind_speed'] / 2.237))
                if description4 == 'Snow':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/sn.ico'
                elif description4 == 'Sleet':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/sl.ico'
                elif description4 == 'Hail':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/h.ico'
                elif description4 == 'Thunderstorm':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/t.ico'
                elif description4 == 'Heavy Rain':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/hr.ico'
                elif description4 == 'Light Rain':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/lr.ico'
                elif description4 == 'Showers':
                    url4= 'https://www.metaweather.com/static/img/weather/ico/s.ico'
                elif description4 == 'Heavy Cloud':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/ht.ico'
                elif description4 == 'Light Cloud':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/lc.ico'
                elif description4 == 'Clear':
                    url4 = 'https://www.metaweather.com/static/img/weather/ico/c.ico'

                temperature5 = (round(api_data['consolidated_weather'][4]['the_temp']))
                description5 = (api_data['consolidated_weather'][4]['weather_state_name']) 
                humidity5 = (api_data['consolidated_weather'][4]['humidity'])
                wind_speed5 = (round(api_data['consolidated_weather'][4]['wind_speed'] / 2.237))
                if description5== 'Snow':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/sn.ico'
                elif description5 == 'Sleet':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/sl.ico'
                elif description5 == 'Hail':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/h.ico'
                elif description5 == 'Thunderstorm':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/t.ico'
                elif description5 == 'Heavy Rain':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/hr.ico'
                elif description5 == 'Light Rain':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/lr.ico'
                elif description5 == 'Showers':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/s.ico'
                elif description5 == 'Heavy Cloud':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/ht.ico'
                elif description5 == 'Light Cloud':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/lc.ico'
                elif description5 == 'Clear':
                    url5 = 'https://www.metaweather.com/static/img/weather/ico/c.ico'
            print(url1)
            return render(
                request,
                'weathertwo/index.html',
                {
                    'location': location,
                    'temperature1': temperature1,
                    'description1' : description1,
                    'humidity1' : humidity1,
                    'wind_speed1' : wind_speed1, 
                    'url1' : url1,

                    'location': location,
                    'temperature2': temperature2,
                    'description2' : description2,
                    'humidity2' : humidity2,
                    'wind_speed2' : wind_speed2, 
                    'url2' : url2,

                    'location': location,
                    'temperature3': temperature3,
                    'description3' : description3,
                    'humidity3' : humidity3,
                    'wind_speed3' : wind_speed3, 
                    'url3' : url3,

                    'location': location,
                    'temperature4': temperature4,
                    'description4' : description4,
                    'humidity4' : humidity4,
                    'wind_speed4' : wind_speed4, 
                    'url4' : url4,

                    'location': location,
                    'temperature5': temperature5,
                    'description5' : description5,
                    'humidity5' : humidity5,
                    'wind_speed5' : wind_speed5, 
                    'url5' : url5,
                }
            )

    else:
        form = LocationForm()

    return render(request, 'weathertwo/index.html', {'form': form})

    
