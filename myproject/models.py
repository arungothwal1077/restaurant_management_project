#myproject/urls.py
from django.contrib import admin
from djnago.urls import path
from django.shortcuts import render


#view function 
def home(request):
    context = {
        'restaurant_name' : 'Chtkara Bites'
        'message': 'welcome to our restaurant'
    }
    return render(request, 'home.html', context)


# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home name= 'home'),

]

"""
 creat a file : template/home.html
<!DOCTYPE html>
<html>
<head>
     <title>{{ restauranrt_name }}</title>
</head>
<body>
    <h1>{{ restaurant_name }}</h1>
    <p>{{ message }}</p>
</body>
<html>
"""