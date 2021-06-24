from django.db import router
from django.urls import path, include
from .views import * 


urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('agregar', agregar_producto, name="agregar"),
    path('listar', listar_producto, name="listar"),
    path('agregar_bajo', agregar_bajo, name="agregar-bajo"),
    path('agregar_piano', agregar_piano, name="agregar-piano"),
    path('agregar_percusion', agregar_percusion, name="agregar-percusion"),
    path('agregar_amplificador', agregar_amplificador, name="agregar-amplificador"),
    path('agregar_accesorio', agregar_accesorio, name="agregar-accesorio"),
    path('registro', registro, name="registro"),
   
]