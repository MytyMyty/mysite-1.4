from polls.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #Conseguir la session key si esta existe
        cart = self.session.get('session_key')
        
        #Si no existe, se crea una!
        if 'session_key' not in request.session:
            cart =self.session['session_key'] = {}
        
        
        #Asegurar que el cart funciona en todas las paginas del sitio    
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        #Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        
        total=0
        for key,value in quantities.items():
            key = int(key)
            for product in products:
                if key == product.id:
                    total = total + (product.preciod * value)
        return total    
        
    def __len__(self) :
        return len(self.cart)
    
    def get_prods(self):
        #Obtener los IDs de los productos en el carrito
        product_ids = self.cart.keys()
        #Usar los IDs para buscar productos en la DB
        products = Product.objects.filter(id__in=product_ids)
        
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        ourcart= self.cart
        
        ourcart[product_id] = product_qty	
        self.session.modified = True
        thing= self.cart
        return thing
    
    def remove(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
        