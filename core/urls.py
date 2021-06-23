from django.urls import path
from . import views
from .views import home, crearDireccion, form_mod_direccion, Ver, form_del_direccion

urlpatterns = [
	path('', views.home, name="home"),
	path('ingresar/', views.ingresar, name='ingresar'),
    path('loggedin/', views.loggedin, name='loggedin'),
	path('agregardireccion/', views.agregardireccion, name='agregardireccion'),
	path('nodisponible/', views.nodisponible, name='nodisponible'),
	path('crear_direccion', crearDireccion, name="crear_direccion"),
	path('ver',Ver, name="ver"),
	path('form_mod_direccion/<id>', form_mod_direccion, name="form_mod_direccion"),
	path('form_del_direccion/<id>', form_del_direccion, name="form_del_direccion")
]