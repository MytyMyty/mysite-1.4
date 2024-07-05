from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product, Review, Categorias
from . forms import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def home(request):
    products= Product.objects.all()

    context={
        'products': products
    }
    return render(request, "pages/index.html" , context=context)

def allProducts(request):
    products= Product.objects.all()

    context={
        'products': products
    }
    return render(request, "pages/allProducts.html" , {'products': products} )

def category(request, foo):
    foo = foo.replace('-', ' ')
    
    try:
        #Buscar categoria
        category = Categorias.objects.get(name=foo)
        products = Product.objects.filter(categorias=category)
        return render(request, 'pages/categoria.html', {'category': category, 'products': products})
        
    except:
        messages.success(request, 'Categoría no encontrada')
        return redirect('home')

def is_admin_or_moderator(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin_or_moderator, login_url='home')

def addProduct(request):
    form= ProductForm()

    if request.method =='POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        messages.success(request, 'Error al agregar el producto')


    context ={ "form":form}

    return render(request, 'admin_pages/addProduct.html', context)

def admInd(request):
    return render(request, 'admin_pages/admindex.html')



def detalleProduct(request, pk):
    product = Product.objects.get(id=pk)
    
    reviews = Review.objects.filter(product=product)

    context = {
        'reviews': reviews,
        'product': product
    }

    return render(request, 'pages/detalleProduct.html', context)

def Review_rate(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product= Product.objects.get(id=product_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user= request.user
        Review(user=user, product=product, comment=comment, rate=rate).save()
        return redirect('detalleProduct', id=product_id)
        