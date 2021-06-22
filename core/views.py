from django.shortcuts import render
from .models import Direccion,TipoCasa,Calle

# Create your views here.
def home(request):
    direcciones= Direccion.objects.all()

    return render (request , 'home.html', context={'direccione':direcciones})

def ingresar(request):
    direcciones= Direccion.objects.all()

    return render (request , 'ingresar.html', context={'direccione':direcciones})

def loggedin(request):
    direcciones= Direccion.objects.all()

    return render (request , 'loggedin.html', context={'direccione':direcciones})

def agregardireccion(request):
    direcciones= Direccion.objects.all()

    return render (request , 'agregardireccion.html', context={'direccione':direcciones})

def nodisponible(request):

    return render (request , 'nodisponible.html')