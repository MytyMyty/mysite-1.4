from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Miembros
# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Exito al iniciar Sesion"))
            return redirect('home')
        else:
            messages.success(request, ("Hubo un Error iniciando Sesion, Intente de nuevo..."))
            return redirect('login')
    else:
        return render(request, 'autenticacion/formulario.html',{})

def cerrar_cesion(request):
    logout(request)
    messages.success(request,("Su cesion ha sido cerrada"))
    return redirect('home')

def registrar_usuario(request):
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Se ha registrado correctamente!!"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request,'autenticacion/registro.html',{
        'form': form ,

    })

def crud (request):
    miembros = Miembros.objects.all()
    context= {'miembros':miembros}
    return render (request, 'miembros/miembros_list.html', context)
def miembrosAdd(request):
    if request.method != "POST":
        miembros=Miembros.objects.all()
        context={'miembros':miembros}
        return render(request, 'miembros/miembros_add.html', context)
    else:
        rut=request.POST["rut"]
        mail=request.POST["mail"]
        nombre=request.POST["nombre"]
        apellidos=request.POST["apellidos"]
        fecnac=request.POST["fecnac"]
        activo="1"

        obj=Miembros.objects.create( rut=rut, mail=mail, nombre=nombre, apellidos=apellidos, fecnac=fecnac, activo=1 )

        obj.save()
        context={'mensaje': "Datos grabados..."}
        return render(request, 'miembros/miembros_add.html', context)
def miembros_del(request,pk):
    context={}
    try:
        miembros=Miembros.objects.get(rut=pk)

        miembros.delete()
        mensaje="Datos eliminados..."
        miembros= Miembros.objects.all()
        context = {'miembros': miembros, 'mensaje' : mensaje}
        return render(request, 'miembros/miembros_list.html', context)
    except:
        mensaje="Error, Rut no existente..."
        miembros = Miembros.objects.all()
        context= {'miembros' : miembros, 'mensaje' : mensaje}
        return render(request, 'miembros/miembros_list.html', context)
    
def miembros_findEdit(request,pk):
    if pk != "":
        miembros= Miembros.objects.get(rut=pk)
        
        context={'miembros': miembros}
        if miembros:
            return render(request,'miembros/miembros_edit.html', context)
        else:
            context={'mensaje': "Error, Rut no existente..."}
            return render(request, 'miembros/miembros_list.html', context)
def miembrosUpdate(request):
    if request.method == "POST":

        rut=request.POST["rut"]
        mail=request.POST["mail"]
        nombre=request.POST["nombre"]
        apellidos=request.POST["apellidos"]
        fecnac=request.POST["fecnac"]
        activo="1"

        miembro= Miembros()
        miembro.rut=rut
        miembro.mail=mail
        miembro.nombre=nombre
        miembro.apellidos=apellidos
        miembro.fecnac=fecnac
        miembro.activo=1
        miembro.save()

        context={'mensaje': "Datos actualizados...", 'miembro':miembro}
        return render(request, 'miembros/miembros_edit.html', context)
    
    else:
        miembros=Miembros.objects.all()
        context={'miembros':miembros}
        return render (request,'miembros/miembros_list.html',context)
        
