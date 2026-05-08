# Agro Service — Aplicación web Django

Plataforma de servicios agrícolas para la contratación y agendado de citas.

---

## 📁 Estructura del proyecto

```
agro_service/
│
├── agro_service/          # Configuración central del proyecto
│   ├── settings.py        # Variables de configuración
│   ├── urls.py            # Rutas principales (delega a cada app)
│   └── wsgi.py
│
├── servicios/             # App: catálogo de servicios
│   ├── models.py          # Modelo Servicio
│   ├── views.py           # Vistas: inicio, catálogo, detalle
│   ├── urls.py
│   ├── admin.py
│   └── fixtures/          # Datos iniciales para cargar con loaddata
│
├── contacto/              # App: formulario de contacto
│   ├── models.py          # Modelo MensajeContacto
│   ├── forms.py           # Formulario de contacto
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cesta/                 # App: cesta y agendado de citas
│   ├── models.py          # Modelos Cita e ItemCita
│   ├── forms.py           # Formulario de datos del cliente
│   ├── views.py           # Lógica de sesión para la cesta
│   ├── urls.py
│   ├── admin.py
│   └── context_processors.py  # Contador de cesta en toda la web
│
├── templates/             # Templates HTML
│   ├── base/base.html     # Template padre (nav, mensajes, footer)
│   ├── servicios/
│   ├── contacto/
│   └── cesta/
│
├── static/
│   └── css/main.css       # Estilos base
│
├── manage.py
└── requirements.txt
```

---

## 💡 Flujo de usuario

1. El cliente visita la web y ve los **servicios disponibles**
2. Añade uno o más servicios a la **cesta** (guardada en sesión)
3. Desde la cesta, completa el **formulario de cita** con sus datos y fecha deseada
4. La cita queda guardada en la base de datos con estado **"Pendiente"**
5. Tú la gestionas desde el **panel de administración** (/admin)
6. El precio final se ajusta tras el trabajo (no hay pago online)
