from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):
    """
    Formulario para completar la cita al finalizar la cesta.
    """

    class Meta:
        model = Cita
        fields = [
            'nombre_cliente', 'email_cliente', 'telefono_cliente',
            'descripcion_parcela', 'kilos_estimados', 'fecha_deseada', 'notas'
        ]
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'telefono_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '600 000 000'}),
            'descripcion_parcela': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'placeholder': 'Dirección o cómo llegar a tu parcela'
            }),
            'kilos_estimados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 50000'}),
            'fecha_deseada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notas': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 2,
                'placeholder': 'Cualquier observación adicional (opcional)'
            }),
        }
        labels = {
            'nombre_cliente': 'Nombre',
            'email_cliente': 'Correo electrónico',
            'telefono_cliente': 'Teléfono de contacto',
            'descripcion_parcela': 'Ubicación de la parcela',
            'kilos_estimados': 'Kilos estimados',
            'fecha_deseada': 'Fecha deseada',
            'notas': 'Notas adicionales',
        }
