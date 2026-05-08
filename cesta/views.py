from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from servicios.models import Servicio
from .forms import CitaForm


# ──────────────────────────────────────────────
# Helpers para manejar la cesta en la sesión
# La cesta se guarda en request.session como una lista de IDs de servicio
# Ejemplo: request.session['cesta'] = [1, 3]
# ──────────────────────────────────────────────

def _get_cesta(request):
    """Devuelve la lista de IDs de servicios en la cesta."""
    return request.session.get('cesta', [])


def _save_cesta(request, cesta):
    """Guarda la cesta en la sesión."""
    request.session['cesta'] = cesta
    request.session.modified = True  # Forzar guardado


# ──────────────────────────────────────────────
# Vistas
# ──────────────────────────────────────────────

def ver_cesta(request):
    """Muestra los servicios añadidos a la cesta."""
    ids_cesta = _get_cesta(request)
    servicios = Servicio.objects.filter(id__in=ids_cesta, activo=True)
    return render(request, 'cesta/cesta.html', {'servicios': servicios})


def añadir_a_cesta(request, servicio_id):
    """Añade un servicio a la cesta (si no estaba ya)."""
    cesta = _get_cesta(request)

    if servicio_id not in cesta:
        # Comprobamos que el servicio existe antes de añadirlo
        get_object_or_404(Servicio, pk=servicio_id, activo=True)
        cesta.append(servicio_id)
        _save_cesta(request, cesta)
        messages.success(request, 'Servicio añadido a la cesta.')
    else:
        messages.info(request, 'Este servicio ya está en tu cesta.')

    return redirect('ver_cesta')


def quitar_de_cesta(request, servicio_id):
    """Elimina un servicio de la cesta."""
    cesta = _get_cesta(request)
    if servicio_id in cesta:
        cesta.remove(servicio_id)
        _save_cesta(request, cesta)
        messages.success(request, 'Servicio eliminado de la cesta.')

    return redirect('ver_cesta')


def confirmar_cita(request):
    """Procesa el formulario final para agendar la cita."""
    ids_cesta = _get_cesta(request)

    if not ids_cesta:
        messages.warning(request, 'Tu cesta está vacía. Añade algún servicio primero.')
        return redirect('catalogo')

    servicios = Servicio.objects.filter(id__in=ids_cesta, activo=True)

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
            # Asociamos los servicios a la cita
            from .models import ItemCita
            for servicio in servicios:
                ItemCita.objects.create(cita=cita, servicio=servicio)

            # Vaciamos la cesta tras confirmar
            _save_cesta(request, [])

            messages.success(
                request,
                f'¡Cita agendada correctamente para el {cita.fecha_deseada.strftime("%d/%m/%Y")}! '
                'Nos pondremos en contacto contigo para confirmar.'
            )
            return redirect('cita_confirmada', pk=cita.pk)
        else:
            messages.error(request, 'Revisa los datos del formulario.')
    else:
        form = CitaForm()

    return render(request, 'cesta/confirmar_cita.html', {
        'form': form,
        'servicios': servicios,
    })


def cita_confirmada(request, pk):
    """Página de confirmación después de agendar la cita."""
    from .models import Cita
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, 'cesta/cita_confirmada.html', {'cita': cita})
