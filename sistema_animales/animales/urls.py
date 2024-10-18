from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('eliminar_animal/<int:animal_id>/', views.eliminarAnimal, name='eliminar_animal'),
    path('cerrarSesion/', views.CerrarSesion, name='cerrarSesion'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
]