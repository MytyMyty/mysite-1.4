from django.urls import path, re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('allProducts', views.allProducts, name="allProducts"),
    
    path("addProduct", views.addProduct, name="addProduct"),
    
    path("admin_index", views.admInd , name="admInd"),
    
    path('product/<int:pk>', views.detalleProduct, name="detalleProduct"),
    
    path('review/', views.Review_rate, name="review"),
    
    path('category/<str:foo>', views.category, name="category"),
    
]