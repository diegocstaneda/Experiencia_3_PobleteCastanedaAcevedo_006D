from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('ingresar/', views.ingresar, name='ingresar'),
    path('loggedin/', views.loggedin, name='loggedin'),
	path('agregardireccion/', views.agregardireccion, name='agregardireccion'),
	path('nodisponible/', views.nodisponible, name='nodisponible'),
]