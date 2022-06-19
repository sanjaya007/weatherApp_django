from django.shortcuts import render, redirect
from datetime import date, datetime
from app.models import Weather
import requests

# Create your views here.
def index(request):
    errorMsg = None
    def dateFormat():
        today = date.today()
        return today.strftime("%B %d, %Y")

    if request.method == "POST":
        place = request.POST.get('search')   
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ place +'&units=metric&appid=ec765c99d16a5d08c9a1ecbd9c815f82&fbclid=IwAR2ofJAU700g9EGd0Kex87S6QHLo_WL08-7ARanf7DM0ISIG3pe_x4GTDhs')
        data = response.json()
        
        if response.status_code == 200:
            def convertToKmPerHr(value):
                return format(value * 18/5, ".2f")

            def timeFormat():
                now = datetime.now()
                return now.strftime("%H:%M")

            dataToSave = Weather(
               place = data['name'],
               country = data['sys']['country'], 
               status = data['weather'][0]['main'],
               icon = data['weather'][0]['icon'],
               description = data['weather'][0]['description'].title(),
               temperature = data['main']['temp'],
               humidity = data['main']['humidity'],
               wind_speed = convertToKmPerHr(data['wind']['speed']),
               date = dateFormat(),
               time = timeFormat()
            )
            dataToSave.save()
            return redirect('/')
        else:
            errorMsg = True



    weatherArr = []
    countData = Weather.objects.count()

    if countData:
        weatherData = Weather.objects.all()
        for value in weatherData:
            weatherArr.append(value)
        context = {
        'weatherArr': weatherArr,
        'errorMsg' : errorMsg,
        'date': dateFormat()
        }
    else:
        
        context = {
        'weatherArr': weatherArr,
        'errorMsg' : errorMsg,
        'noData': True,
        'date': dateFormat()
        }
        

    return render(request, 'index.html', context)