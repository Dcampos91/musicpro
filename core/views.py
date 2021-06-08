from django.shortcuts import render
from .models import *
from .forms import ContactoForm
from rest_framework import viewsets
from .serializers import GuitarraSerializer

#clases de serializer
class GuitarraViewset(viewsets.ModelViewSet):
    queryset = Guitarra.objects.all()
    serializer_class = GuitarraSerializer





#fin serializer

def home(request):
    guitarra = Guitarra.objects.all()
    bajo = Bajo.objects.all()
    piano = Piano.objects.all()
    percusion = Percusion.objects.all()
    amplificador = Amplificador.objects.all()
    accesorios = Accesorio.objects.all()
    data = {
        'guitarra':guitarra,
        'bajo':bajo,
        'piano':piano,
        'percusion':percusion,
        'amplificador':amplificador,
        'accesorios':accesorios
    }
    return render(request, 'core/home.html', data)

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

