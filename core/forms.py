from django import forms
from django.forms import ModelsForm
from .models import Direccion

class DireccionForm(ModelsForm):

    class Meta:
        model = Direccion
        fields = ['nombre', 'direccion', 'Comuna', 'numedirec', 'telefono' , 'Calle', 'TipoCasa'] 
