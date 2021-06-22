from django.urls import path
from . import views
from .views import form_direccion

urlpatterns = [
	path('', views.home, name="home"),
	path('ingresar/', views.ingresar, name='ingresar'),
    path('loggedin/', views.loggedin, name='loggedin'),
	path('agregardireccion/', views.agregardireccion, name='agregardireccion'),
	path('nodisponible/', views.nodisponible, name='nodisponible'),
	path('form_direccion', form_direccion, name="form_direccion")
]