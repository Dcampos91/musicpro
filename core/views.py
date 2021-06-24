from django.shortcuts import redirect, render
from .models import *
from .forms import *
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth import authenticate, login
from django.contrib import messages



def contacto(request):
    data = {
       'form': ContactoForm() 
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje enviado"
        else:
            data["form"] = formulario
            
    return render(request, 'core/contacto.html', data)

def agregar_producto(request):

    return render(request, 'core/producto/agregar.html')
def agregar_bajo(request):

    return render(request, 'core/producto/agregar_bajo.html')
def agregar_piano(request):

    return render(request, 'core/producto/agregar_piano.html')
def agregar_percusion(request):

    return render(request, 'core/producto/agregar_percusion.html')
def agregar_amplificador(request):

    return render(request, 'core/producto/agregar_amplificador.html')
def agregar_accesorio(request):

    return render(request, 'core/producto/agregar_accesorio.html')

def listar_producto(request):
  
    return render(request, 'core/producto/listar.html')

def home(request):
    data = {
        'guitarra': get_guitarra(),
        'bajo': get_bajo(),
        'piano': get_piano(),
        'percusion': get_percusion(),
        'amplificador': get_amplificador(),
        'accesorio':get_accesorio()
    }
    return render(request, 'core/home.html',data)

def registro(request):
    data = {
        'form' : CustomUserCrationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCrationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)