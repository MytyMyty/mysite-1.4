from django.db import models

class Product(models.Model):
    image= models.ImageField(null=False, blank=False)
    marca=models.CharField(max_length=9,null=False, blank=False)
    name=models.CharField(max_length=35, null=False, blank=False)
    precio=models.DecimalField(max_digits=7, decimal_places=3)
    preciod=models.DecimalField(max_digits=7, decimal_places=3)
    es_publicado= models.BooleanField(default=True)
    fecpub=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    