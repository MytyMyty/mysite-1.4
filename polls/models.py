from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


class Categorias(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) :
        return self.name
    
    

class Product(models.Model):
    categorias = models.ForeignKey(Categorias, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    image= models.ImageField(null=False, blank=False, upload_to='')
    marca=models.CharField(max_length=9,null=False, blank=False)
    name=models.CharField(max_length=68, null=False, blank=False)
    descripcion=models.TextField(max_length=140, null=False, blank=False, default="Esto es un texto de descripcion base acerca de este gran producto, es perfecto para ti y se adecua a tu estilo")
    precio=models.DecimalField(max_digits=1000, decimal_places=3)
    preciod=models.DecimalField(max_digits=1000, decimal_places=3)
    es_publicado= models.BooleanField(default=True)
    es_stock=models.BooleanField(default=True)
    fecpub=models.DateTimeField(auto_now_add=True)
    fecupd=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Products'	
        ordering = ('-fecpub',)

    def __str__(self):
        return self.name

class RatingC(models.IntegerChoices) :
    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    __empty__ = 'Ninguna'
    
class Review(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField(max_length=300)
    rate= models.IntegerField( choices=RatingC, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta :
        verbose_name_plural = "Product Reviews"
    def __str__(self) :
        return self.product.name
    
    def get_rating(self) :
        return self.rate
