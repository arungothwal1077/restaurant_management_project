#myproject/urls.py
from djnago.contrib import admin 
from django.urls import path
from django.shortcuts import render

def home(request):
    context = {
        'restaurant_name': 'Chatkara Bites',
        'message': 'Welcome to our restaurant',
        'phone': '+91-9068245991'
    }
    return render(request, 'home.html', context)


urlpatterns = {
    path('admin/', admin.site.urls),
    path('',home,name='home'),
}
"""

#templates/home.html
<!DOTYPE html>
<html>
<head>
   <title{{ restauranrt_name }}</title>
   <style>
   body { font-family: Arial, sans; bakground:#f9f9f9; text-align:centre; padding:50pxl; }
   h1 { color:#2ce50; margin-bottom:10px; }
   p{ color:#555; font-size:18px; margin:5px; }
   .phone { margin-top:15px; font-weight;bold; color:#2980b9; }
  </style>
<body>
   <h1>{{ restaurant_name }}</h1>
   <p>{{ messsage }}</p>
   <p class= "phone"> {{ phone }}</p>
</body>
</html>
"""