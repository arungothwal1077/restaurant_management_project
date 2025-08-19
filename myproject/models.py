#myproject/urls.py
from django.contrib import admin
from djnago.urls import path
from django.shortcuts import render


#view function for home page
def home(request):
    context = {
        'restaurant_name' : 'Chtkara Bites'
        'message': 'welcome to our restaurant'
        'phone': settings.PHONE_NUMBER
    }
    return render(request, 'home.html', context)

#view function for contact page
def contact(request):
    context = {
        'email': 'support@chatkarabites.com',
        'phone': '+91-9068245991',
        'address': '123 Main Street , Jaipur , India'
}
return render(request, 'contact.html',context)

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home name= 'home'),

]

"""
#templates/hpme.html
<!DOCTYPE html>
<html>
<head>
     <title>{{ restauranrt_name }}</title>
</head>
<body>
    <h1>{{ restaurant_name }}</h1>
    <p>{{ message }}</p>
    <a> href='/contact/">contact/ Us</a>
</body>
<html>
#templates/contact.html
</head>
<body>
    <h1>Contact Us</h1>
    <p>Email: {{ email }}</p>
    <p>Address: {{ address }}</a>
</body>
</html>
"""