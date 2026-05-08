from django.contrib import admin
from .models import Servicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_por_kg', 'categoria', 'activo']
    list_filter = ['categoria', 'activo']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['activo']  # Permite activar/desactivar desde el listado
