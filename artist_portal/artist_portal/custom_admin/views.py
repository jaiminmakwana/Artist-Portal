from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
import sqlite3
import os
from django.contrib.auth.models import User
from Home.models import Profile
from django.http import HttpResponse,HttpResponseRedirect
from products.models import Product,Category,Ratings
from .forms import CatForm
from django.contrib import messages
from cart.models import Cart
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.session.get('admin'):
        template = 'custom_admin/index.html'
        return render(request,template)
    else:
        return redirect('Admin:login')


def users(request):
    template = 'custom_admin/users.html'
    if request.session.get('admin'):
        users = User.objects.all()
        return render(request,template,{'users':users})
    else:
        return redirect('Admin:login')

def cat(request):
    template = 'custom_admin/Category.html'
    if request.session.get('admin'):
        category = Category.objects.all()
        return render(request,template,{'categories':category})
    else:
        return redirect('Admin:login')


def login(request):
    template = 'custom_admin/login.html'
    if request.method == 'POST':
        user = request.POST['username']
        pwd = request.POST['password']
        if user=='admin' and pwd=='admin':
            request.session['admin'] = user
            return redirect('Admin:home')

    return render(request,template)


def logout(request):
    template = 'custom_admin/logout.html'
    if request.session.get('admin') != None:
        request.session.delete()
        return redirect('Admin:login')
    else:
        return redirect('Admin:login')

    return render(request,template)


def profile(request,pk):
    template = 'custom_admin/user_profile.html'
    if request.session.get('admin'):
        user = User.objects.get(pk=pk)
        return render(request,template,{'user':user})
    else:
        return redirect('Admin:login')


def user_products(request,pk):
    template = 'custom_admin/user_products.html'
    if request.method == 'POST':
        if request.session.get('admin'):
            print('I am admin')
            usr = User.objects.get(pk=pk)
            print(usr)
            products = Product.objects.filter(user__username=usr.username)
            print(list(products))
            return render(request,template,{'products':products})

    return HttpResponse(1)



def add_cat(request):
    if request.session.get('admin'):
        if request.method == "POST":
            form = CatForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, "Category is added Successfully..")
                return redirect('Admin:home')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = CatForm()
        template = 'custom_admin/add_category.html'
        return render(request, template, {'form': form})
    else:
        return redirect('Admin:login')




def products(request):
    template = 'custom_admin/products.html'
    if request.session.get('admin'):
        product = Product.objects.all()
        return render(request,template,{'products':product})
    else:
        return redirect('Admin:login')


def ratings(request):
    template = 'custom_admin/ratings.html'
    if request.session.get('admin'):
        rating = Ratings.objects.all()
        return render(request,template,{'ratings':rating})
    else:
        return redirect('Admin:login')



def order(request):
    template = 'custom_admin/order.html'
    if request.session.get('admin'):
        order = Cart.objects.all()
        return render(request,template,{'orders':order})
    else:
        return redirect('Admin:login')


def manage_users(request):
    template = 'custom_admin/manage_users.html'
    if request.session.get('admin'):
        users = User.objects.all()
        return render(request,template,{'users':users})
    else:
        return redirect('Admin:login')


def delete_user(request,pk):
    template = 'custom_admin/delete_user.html'
    user = get_object_or_404(User,pk=pk)
    print(user)
    print(user.email)
    if request.method == 'POST':
        user.delete()
        messages.success(request,'User deleted successfully')
        subject = 'Hello ' + str(user.name) + ' from artist_portal!'
        message = 'Your account has been deleted from our website due to some mischiefs you have done on our website. Please contact us through the contact form from our website to know the reson why we have deleted your account.'
        email_from = settings.EMAIL_HOST_USER
        email_to = [user.email,]
        print(email_to)
        send_mail(subject, message, email_from, email_to)
        messages.success(request, 'Form submitted successfully.')
        return redirect('Admin:manage_users')
    return render(request,template)


def manage_category(request):
    template = 'custom_admin/manage_category.html'
    if request.session.get('admin'):
        category = Category.objects.all()
        return render(request,template,{'categories':category})
    else:
        return redirect('Admin:login')


def delete_category(request,pk):
    template = 'custom_admin/delete_category.html'
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request,'Category deleted successfully')
        return redirect('Admin:manage_category')
    return render(request,template)