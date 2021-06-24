from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
class Guitarraform(forms.ModelForm):

    class Meta:
        model = Guitarra
        fields = '__all__'

class Bajoform(forms.ModelForm):

    class Meta:
        model = Bajo
        fields = '__all__'

class Pianoform(forms.ModelForm):

    class Meta:
        model = Piano
        fields = '__all__'

class Percusionform(forms.ModelForm):

    class Meta:
        model = Percusion
        fields = '__all__'

class Amplificadorform(forms.ModelForm):

    class Meta:
        model = Amplificador
        fields = '__all__'

class Accesorioform(forms.ModelForm):

    class Meta:
        model = Accesorio
        fields = '__all__'

class CustomUserCrationForm(UserCreationForm):
    pass
