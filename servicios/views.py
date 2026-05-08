from django.shortcuts import render
from .models import Servicio


def inicio(request):
    """Página principal con presentación de la empresa."""
    servicios = Servicio.objects.filter(activo=True)
    context = {
        'servicios': servicios,
    }
    return render(request, 'servicios/inicio.html', context)


def catalogo(request):
    """Catálogo completo de servicios disponibles."""
    servicios = Servicio.objects.filter(activo=True)
    context = {
        'servicios': servicios,
    }
    return render(request, 'servicios/catalogo.html', context)


def detalle_servicio(request, pk):
    """Detalle de un servicio concreto."""
    from django.shortcuts import get_object_or_404
    servicio = get_object_or_404(Servicio, pk=pk, activo=True)
    context = {
        'servicio': servicio,
    }
    return render(request, 'servicios/detalle.html', context)
