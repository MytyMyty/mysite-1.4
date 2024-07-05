from .cart import Cart

#Crear un context-proccesor para que el cart funcione en todas las paginas
def cart(request):
    #Devolver la data del cart
    return {'cart': Cart(request)}