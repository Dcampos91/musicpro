from django.db import router
from django.urls import path, include
from .views import * 
from rest_framework import routers
#crear las urls necesarios para el rest
router = routers.DefaultRouter()
router.register('guitarra', GuitarraViewset)

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('api/', include(router.urls)),
]