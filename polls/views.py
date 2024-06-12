from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product
from . forms import ProductForm

# Create your views here.

def home(request):
    products= Product.objects.all()

    context={
        'products': products
    }
    return render(request, "pages/index.html" , context=context)
def registro(request):
    context={}
    return render(request, "pages/registro.html" , context)
def iniciosesion(request):
    context={}
    return render(request, "pages/formulario.html" , context)
def camisetas(request):
    context={}
    return render(request, "pages/camisetas.html" , context)
def botines(request):
    context={}
    return render(request, "pages/botines.html" , context)
def guantes(request):
    context={}
    return render(request, "pages/guantes.html" , context)

def addProduct(request):
    form= ProductForm()

    if request.method =='POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()


    context ={ "form":form}

    return render(request, 'addProduct.html', context)
