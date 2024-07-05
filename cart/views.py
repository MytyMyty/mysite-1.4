from django.shortcuts import render, get_object_or_404
from .cart import Cart
from polls.models import Product,Categorias
from django.http import JsonResponse
from django.contrib import messages





def cart_add(request):
    
    cart= Cart(request)
    
    if request.POST.get('action') == 'post':
        #Obtener la id del producto del formulario
        product_id = int(request.POST.get('product_id'))
        product_qty= int(request.POST.get('product_qty'))
        
        #Conseguir producto desde la DB
        product = get_object_or_404(Product, id=product_id)
        
        #Guardar en la sesion el producto
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        
        #Return response
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, 'Producto agregado al carrito')
        return response
def cart_remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.remove(product=product_id)
        #Return response
        response = JsonResponse({'product': product_id})
        return response
def cart_update(request):
    cart= Cart(request)
    
    if request.POST.get('action') == 'post':
        #Obtener la id del producto del formulario
        product_id = int(request.POST.get('product_id'))
        product_qty= int(request.POST.get('product_qty'))
    
        cart.update(product= product_id, quantity=product_qty)
        
        response= JsonResponse({'qty': product_qty})
        return response


def cart_summary(request):
    
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total = cart.cart_total()
    descuento =  request.POST.get('descuento')
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities,"total":total , "descuento":descuento})
    


def descuento(request):
    
    descuento =  request.POST.get('descuento')
    return render(request, "descuento.html", {'descuento': descuento})



