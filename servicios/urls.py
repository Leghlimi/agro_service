from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.catalogo, name='catalogo'),
    path('servicios/<int:pk>/', views.detalle_servicio, name='detalle_servicio'),
]
