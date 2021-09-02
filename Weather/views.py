from django.shortcuts import render
from .models import City
from .Forms import CityForm
import requests
import json
def index(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e309c2d063acbb13b375308f7569d863"
    if request.method=="POST":
        form=CityForm(request.POST)
        form.save()
    form=CityForm()
    Cities=City.objects.all()
    Weatherdata=[]
    for i in Cities:
        data=requests.get(url.format(i)).json()
        Citydata={"city":i.name,
        "temperature":data["main"]["temp"],
        "Description":data["weather"][0]["description"],
        "icon":data["weather"][0]["icon"]}
        Weatherdata.append(Citydata)
    
    x={"Weatherdata":Weatherdata,"form":form}
    return render(request,"Weather/Weather.html",x)

#application programming interface