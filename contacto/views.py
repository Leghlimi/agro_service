from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm


def contacto(request):
    """Muestra y procesa el formulario de contacto."""

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda en la base de datos
            messages.success(request, '¡Mensaje enviado! Nos pondremos en contacto contigo pronto.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor, revisa los campos del formulario.')
    else:
        form = ContactoForm()

    return render(request, 'contacto/contacto.html', {'form': form})
