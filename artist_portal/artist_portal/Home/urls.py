from django.urls import path,include
from .views import Home, about, contact,profile,feedback

app_name = 'Home'

urlpatterns = [
    path('', Home, name='Home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback, name='feedback'),
    path('profile/', profile, name='profile' ),
    path('products/',include('products.urls'))
]