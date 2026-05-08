from django.contrib import admin
from .models import Cita, ItemCita


class ItemCitaInline(admin.TabularInline):
    """Muestra los servicios contratados dentro del detalle de la cita."""
    model = ItemCita
    extra = 0
    readonly_fields = ['servicio']


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'telefono_cliente', 'fecha_deseada', 'kilos_estimados', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'fecha_deseada']
    search_fields = ['nombre_cliente', 'email_cliente', 'telefono_cliente']
    list_editable = ['estado']
    readonly_fields = ['fecha_creacion']
    inlines = [ItemCitaInline]
