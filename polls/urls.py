from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("botines", views.botines, name="botines"),
    path("camisetas",views.camisetas, name="camisetas"),
    path("guantes", views.guantes, name="guantes"),
    path("addProduct/", views.addProduct, name="addProduct")
    
]