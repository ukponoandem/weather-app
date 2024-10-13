from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import json
import urllib.request
# Create your views here.

# def Login(request):
#     if request.method == 'POST':
#         username= request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('index')
#         else:
#             messages.info(request,'credential invaild')
#     else:
#         return render(request,"login.html" ) 
    
    
def index(request):
    if request.method=='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f877e8883f2754d3d1425462eaed6f82').read()
        json_data = json.loads(res)
        
        data={
            'country_code': str(json_data['sys']['country'] ),
            'coordinate':str(json_data['coord']['lon'])+ ''+ str(json_data['coord']['lat']),
            'temp':str(json_data['main']['temp'])+ 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }    
        
    else:
        city="NO result"
        Data={}  
    return render(request,'index.html', {"city":city,"Data":Data})