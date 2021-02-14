from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product,Ratings
from .forms import ProductForm,Rating_Form
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.


def products_list(request):
    products = Product.objects.all()
    template = 'products/shop.html'
    return render(request,template,{'products':products})


@login_required
def productcreate(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None, request.FILES or None)
        if product_form.is_valid():
            f = product_form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Product Added Successfully..')
            return redirect('Home:Home')
        else:
            messages.error(request, 'failed to add Product')
    else:
        product_form = ProductForm()
    template = 'products/createproduct.html'
    return render(request, template, {'product_form': product_form})




def singleproduct(request,pk):
    product = get_object_or_404(Product,pk=pk)
    review = Ratings.objects.filter(product__id=pk)
    template = 'products/singleproduct.html'
    return render(request,template,{'product':product,'ratings':review})



def update_product(request,pk):
    template = 'products/update_product.html'
    product = get_object_or_404(Product,pk=pk)
    form = ProductForm(request.POST or None,request.FILES or None,instance=product)
    if form.is_valid():
        form.save()
        messages.error(request,'Product updated successfully')
        return redirect('Home:Products:my_products')
    return render(request,template,{'product_form': form})


def delete_product(request,pk):
    template = 'products/delete_product.html'
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request,'Product deleted successfully')
        return redirect('Home:Products:my_products')
    return render(request,template)





def my_products(request):
    my_products = Product.objects.filter(user__id=request.user.id)
    template = 'products/my_products.html'
    return render(request,template,{'products':my_products})



def search(request):
    template = 'products/shop.html'
    if "search" in request.GET:
        srh = request.GET["search"]
        # p = request.GET["price"]
        prd = Product.objects.filter(name__contains=srh)  # search by product name
        prd = Product.objects.filter(Q(name__contains=srh)|Q(category__name__contains=srh))
        #prd = Product.objects.filter(Q(name__contains=srh) & Q(price__lt=p)) # search by product name and and pice less than use two search field in html
    return render(request,template,{'products':prd})


def business_photography(request):
    prod = Product.objects.filter(category__name='Business_photography')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def events_photography(request):
    prod = Product.objects.filter(category__name='Events_photography')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def wedding_photography(request):
    prod = Product.objects.filter(category__name='Wedding_photography')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def fashion_photography(request):
    prod = Product.objects.filter(category__name='Fashion_photography')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def pastel_painting(request):
    prod = Product.objects.filter(category__name='Pastel_Painting')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def spray_painting(request):
    prod = Product.objects.filter(category__name='Spray_Painting')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def acrylic_painting(request):
    prod = Product.objects.filter(category__name='Acrylic_Painting')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Pencil_sketch_painting(request):
    prod = Product.objects.filter(category__name='Pencil_sketch_Painting')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Hip_hop_dance(request):
    prod = Product.objects.filter(category__name='Hip_Hop_Dance')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Folk_dance(request):
    prod = Product.objects.filter(category__name='Folk_Dance')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Contemporary_dance(request):
    prod = Product.objects.filter(category__name='Contemporary_Dance')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Classical_dance(request):
    prod = Product.objects.filter(category__name='Classical_Dance')
    template = 'product/shop.html'
    return render(request,template,{'products':prod})

def Lyrics_poetry(request):
    prod = Product.objects.filter(category__name='Lyrics_Poetry')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Narrative_poetry(request):
    prod = Product.objects.filter(category__name='Narrative_Poetry')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Rhymed_poetry(request):
    prod = Product.objects.filter(category__name='Rhymed_Poetry')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Sonnets_poetry(request):
    prod = Product.objects.filter(category__name='Sonnets_Poetry')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Bollywood_music(request):
    prod = Product.objects.filter(category__name='Bollywood_Music')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Instrumental_music(request):
    prod = Product.objects.filter(category__name='Instrumental_Music')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Folk_music(request):
    prod = Product.objects.filter(category__name='Folk_Music')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})

def Classical_music(request):
    prod = Product.objects.filter(category__name='Classical_Music')
    template = 'products/shop.html'
    return render(request,template,{'products':prod})




@login_required
def ratings(request,pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = Rating_Form(request.POST)
        if form.is_valid():
            data = Ratings()
            data.subject = request.POST['subject']
            data.comment = request.POST['comment']
            data.rate = request.POST['rate']
            data.product_id = pk
            usr = request.user
            data.user_id = usr.id
            data.save()
            messages.success(request,'Your Review submitted successfully')
            return HttpResponseRedirect(url)
    else:
        return redirect('account_login')