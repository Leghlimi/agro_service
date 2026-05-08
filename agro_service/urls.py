"""
URLs principales del proyecto Agro Service.

Cada app tiene su propio archivo urls.py que se incluye aquí.
"""

from django.contrib import admin
from django.urls import path, include

# Personalización del panel de administración
admin.site.site_header = "Agro Service"
admin.site.site_title = "Agro Service Admin"
admin.site.index_title = "Panel de administración"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servicios.urls')),
    path('contacto/', include('contacto.urls')),
    path('cesta/', include('cesta.urls')),
]
