from django.db import models


class MensajeContacto(models.Model):
    """
    Guarda los mensajes enviados desde el formulario de contacto.
    """

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)  # Para marcar como leído en el admin

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.fecha_envio.strftime('%d/%m/%Y')}"
