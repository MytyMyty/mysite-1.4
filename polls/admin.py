from django.contrib import admin
from .models import  Categorias,Product,Review

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','marca','categorias', 'name','precio','preciod','es_publicado','es_stock','fecpub','fecupd'] 
    list_filter = ['es_stock','es_publicado']
    list_editable = ['precio','preciod','es_stock','categorias','es_publicado']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'rate', 'created_at']
    readonly_fields = ['created_at']