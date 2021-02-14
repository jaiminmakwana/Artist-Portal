from django.urls import path
from .views import home,users,login,logout,profile,user_products,add_cat,cat,products,ratings,order,manage_users,delete_user,manage_category,delete_category

app_name = 'Admin'

urlpatterns = [
    path('',home,name='home'),
    path('users/',users,name='users'),
    path('cat/',cat,name='cat'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('user_profile/<int:pk>/',profile,name='profile'),
    path('user_products/<int:pk>/',user_products,name='user_products'),
    path('add_cat/',add_cat,name='add_cat'),
    path('products/',products,name='products'),
    path('ratings/',ratings,name='ratings'),
    path('order/',order,name='order'),
    path('manage_users/',manage_users,name='manage_users'),
    path('delete_user/<int:pk>/',delete_user,name='delete_user'),
    path('manage_category/',manage_category,name='manage_category'),
    path('delete_category/<int:pk>/',delete_category,name='delete_category'),
]