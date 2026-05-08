from django import forms
from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    """
    Formulario de contacto. Se genera automáticamente desde el modelo.
    """

    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '600 000 000 (opcional)'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '¿En qué podemos ayudarte?'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'mensaje': 'Mensaje',
        }
