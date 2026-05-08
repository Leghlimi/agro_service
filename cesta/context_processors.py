"""
Context processor para la cesta.

Esto hace que la variable 'cesta_count' esté disponible en TODOS los templates,
sin tener que pasarla manualmente desde cada vista.
Así el icono de la cesta en el menú siempre muestra el número correcto.
"""


def cesta_total(request):
    cesta = request.session.get('cesta', [])
    return {'cesta_count': len(cesta)}
