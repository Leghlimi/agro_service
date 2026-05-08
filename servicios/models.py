from django.db import models


class Servicio(models.Model):
    """
    Representa un servicio agrícola disponible (p.ej. sacar sandías con torillo).
    """

    CATEGORIA_CHOICES = [
        ('sandia', 'Sandía'),
        # En el futuro: ('melon', 'Melón'), ('tomate', 'Tomate'), etc.
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio_por_kg = models.DecimalField(max_digits=6, decimal_places=4)  # Ej: 0.0080
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='sandia')
    activo = models.BooleanField(default=True)  # Para desactivar servicios sin borrarlos
    imagen = models.ImageField(upload_to='servicios/', blank=True, null=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['precio_por_kg']

    def __str__(self):
        return f"{self.nombre} ({self.precio_por_kg}€/kg)"
