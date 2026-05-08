from django.db import models
from servicios.models import Servicio


class Cita(models.Model):
    """
    Representa una cita/pedido agendado por el cliente.
    Sin pago online: el precio final se calcula tras el trabajo en base al peso real.
    """

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente de confirmación'),
        ('confirmada', 'Confirmada'),
        ('en_curso', 'En curso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    # Datos del cliente
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=20)

    # Datos de la parcela
    descripcion_parcela = models.TextField(help_text='Dirección o indicaciones para llegar a la parcela')
    kilos_estimados = models.PositiveIntegerField(help_text='Estimación de kilos a trabajar')

    # Fecha y estado
    fecha_deseada = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, help_text='Observaciones adicionales')

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['fecha_deseada']

    def __str__(self):
        return f"Cita de {self.nombre_cliente} - {self.fecha_deseada}"

    def precio_estimado(self):
        """Calcula el precio estimado en base a los kilos y servicios añadidos."""
        total = sum(
            item.servicio.precio_por_kg * self.kilos_estimados
            for item in self.items.all()
        )
        return total


class ItemCita(models.Model):
    """
    Cada línea de la cesta: qué servicio se solicita para esa cita.
    """
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='items')
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Ítem de cita'
        verbose_name_plural = 'Ítems de cita'
        # Evita añadir el mismo servicio dos veces en la misma cita
        unique_together = ['cita', 'servicio']

    def __str__(self):
        return f"{self.servicio.nombre} en {self.cita}"
