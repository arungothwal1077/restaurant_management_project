#myproject/urls.py
from django.contrib import admin
from djnago.urls import path
from django.shortcuts import render
from djnago.conf import settings


#view function 
def home(request):
    context = {
        'restaurant_name' : 'Chtkara Bites'
        'message': 'welcome to our restaurant'
        'phone': settings.PHONE_NUMBER
    }
    return render(request, 'home.html', context)


# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home name= 'home'),

]

"""
#settins.py (add at bottom)
PHONE_NUMBER = "+919068245991"
 creat a file : template/home.html
<!DOCTYPE html>
<html>
<head>
     <title>{{ restauranrt_name }}</title>
</head>
<body>
    <h1>{{ restaurant_name }}</h1>
    <p>{{ message }}</p>
    <p>contact us: {{ phone }}</p> 
</body>
<html>
"""