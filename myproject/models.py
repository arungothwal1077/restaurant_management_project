#myproject/urls.py
from djnago.contrib import admin 
from django.urls import path
from django.shortcuts import render

#Home view
def home(request):
    context = {
        'restaurant_name': 'Chatkara Bites',
        'message': 'Welcome to our restaurant',
        'phone': '+91-9068245991'
    }
    return render(request, 'home.html', context)


#Menu view
def menu(request):
    menu_items = [
        {'name': 'Paneer Butter Masala','price': '250'},
        {'name': 'Dal Tadka', 'Price': '150'},
        {'name': 'Veg Biryani', 'price': '200'},
        {'name': 'Butter Naan', 'price': '50'},
    ]
    return render(request, 'menu.html',{'menu_items': menu_items})


#URL patterns
urlpatterns = {
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('menu/', menu, name='menu'),
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
   a { display:inline-block; margin-top:20px; padding:10px 20px; background:#2980b9; color#fff; text-decoration:none; border-radius:5px; }
   a:hover { background:#1a5d85; } 

  </style>
<body>
   <h1>{{ restaurant_name }}</h1>
   <p>{{ messsage }}</p>
   <p class= "phone"> {{ phone }}</p>
   <a href="/menu/">See Menu</a>
</body>
</html>

# templates/menu.html
<!DOTYPE html>
<html>
<head>
   <title>Menu</title>
   <style>
    body { font-family: Arial, sans-serif; background;#fff; padding:50px;}
    h1 { color;#2c3e50; text-align:center; margin-bottom:20px; }
    ul { list-system:none; padding:0; max-width:400px; margin:auto; }
    li { background:#f4f4f4; padding:10px; margin:5px 0; border-radius:5px; font-size:18px;}
    a {display:block; text-align:center; margin-top:20px; padding:10px 20px; background:#2980b9; color:fff; text-decoration:none; border-radius:5px;}
    a:hover { background:#1a5d85; }
   </style>
</head>
<body>
   <h1>Our Menu</h1>
   <ul>
    {% for item in menu_items %}
      <li>{{ item.name }} - {{ item.price }}</li>
    {% endfor%}
  </ul>
   <a herf="/">Back to Home</a>
</body> 
</html>
"""