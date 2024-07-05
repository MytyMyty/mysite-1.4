from django import forms
from . models import Categorias,Product
from decimal import Decimal
from django.forms import ModelForm

class CategoriasForm(ModelForm):
    class Meta:
        model = Categorias
        fields = ('name', 'slug')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('categorias','created_by','slug','image', 'marca', 'name','descripcion','precio', 'preciod', 'es_publicado', 'es_stock')
        widgets = {
            'categorias': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'preciod': forms.NumberInput(attrs={'class': 'form-control'}),
            'es_publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'es_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }
    
    def clean_preciod(self):
        precio = self.cleaned_data.get('precio')
        preciod = self.cleaned_data.get('preciod')
        if precio and preciod:
            preciod = round((precio-(precio*preciod/100))/1000, 1)
            preciod = round((Decimal("0.09")+preciod),3)
            precio = round((precio/1000), 3)
            self.cleaned_data['precio'] = precio 
            self.cleaned_data['preciod'] = preciod 
            
        return preciod
               
            
    