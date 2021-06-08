from django.db.models import fields
from .models import *
from rest_framework import serializers

class GuitarraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitarra
        fields = '__all__'