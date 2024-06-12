from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('image', 'marca', 'name', 'precio','preciod', 'es_publicado')
        widgets = {
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'preciod' : forms.TextInput(attrs={'class': 'form-control'}),

        }
        
               
            
    