from django import forms
from django.forms.models import ModelChoiceField
from django.forms import ModelForm, widgets
from .models import Direccion

class DireccionForm(ModelForm):

    class Meta:
        model = Direccion
        fields = ['nombre', 'direccion', 'comuna', 'numedirec', 'telefono' , 'calle', 'tipocasa'] 

        labels  = {
            'nombre': 'Nombre ',
            'direccion': 'Direccion ',
            'comuna': 'Comuna ',
            'numedirec': 'Numero Direccion ',
            'telefono': 'Telefono ',
            'calle': 'Calle',
            'tipocasa': 'Tipo domicilio '

        }

        widgets={

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su nombre',
                    'id': 'nombre'
                }
            ),

            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su direccion',
                    'id': 'direccion'
                }
            ),

            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su comuna',
                    'id': 'comuna'
                }
            ),
            'numedirec': forms.TextInput(  
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su numero de direccion',
                    'id': 'numerodireccion'
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite su numero de telefono',
                    'id': 'telefono'
                }
            ),

            'calle': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'calle'
                }
            ),

            'tipocasa': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipocasa'
                }
            ),


        }
