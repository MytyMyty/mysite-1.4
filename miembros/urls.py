
from django.urls import  path
from . import views
urlpatterns = [ 
    path('login_user', views.login_user, name="login"),
    
    path('cerrar_cesion',views.cerrar_cesion, name='logout'),
    
    path('registrar_user', views.registrar_usuario, name='registrar_user'),
    
    path("crud", views.crud, name ="crud"),
    
    path("miembrosAdd", views.miembrosAdd, name="miembrosAdd"),
    
    path('miembros_del/<str:pk>', views.miembros_del, name= 'miembros_del'),
    
    path('miembros_findEdit/<str:pk>', views.miembros_findEdit, name='miembros_findEdit'),
    
    path('miembrosUpdate', views.miembrosUpdate, name='miembrosUpdate'),
    
]

