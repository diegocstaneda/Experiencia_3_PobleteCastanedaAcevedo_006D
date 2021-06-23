from django.shortcuts import render,redirect
from .models import Direccion,TipoCasa,Calle
from .forms import DireccionForm

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

def crearDireccion(request):
    if request.method=='POST':
        direccion_form = DireccionForm(request.POST)
        if direccion_form.is_valid():
            direccion_form.save()
            return redirect('home')

    else:
        direccion_form=DireccionForm()
    return render(request, 'core/form_creardireccion.html',{'direccion_form':direccion_form})


    
def Ver(request): 
    
    direcciones = Direccion.objects.all()
    return render(request, 'core/ver.html', {'direcciones':direcciones})

def form_mod_direccion(request, id):

    direccion=Direccion.objects.get(nombre=id)

    datos ={
        'form': DireccionForm(instance=direccion)
    }
    if request.method == 'POST': 
        formulario = DireccionForm(data=request.POST, instance = direccion)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_direccion.html',datos)

def form_del_direccion(request,id):
    direccion=Direccion.objects.get(nombre=id)
    direccion.delete()
    return redirect('ver')