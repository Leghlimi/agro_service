from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_cesta, name='ver_cesta'),
    path('añadir/<int:servicio_id>/', views.añadir_a_cesta, name='añadir_a_cesta'),
    path('quitar/<int:servicio_id>/', views.quitar_de_cesta, name='quitar_de_cesta'),
    path('confirmar/', views.confirmar_cita, name='confirmar_cita'),
    path('confirmada/<int:pk>/', views.cita_confirmada, name='cita_confirmada'),
]
