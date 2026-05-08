# Agro Service — Aplicación web Django

Plataforma de servicios agrícolas para la contratación y agendado de citas.

---

## 🚀 Puesta en marcha (paso a paso)

### 1. Crear y activar el entorno virtual
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Aplicar las migraciones (crea las tablas en la base de datos)
```bash
python manage.py migrate
```

### 4. Cargar los servicios iniciales
```bash
python manage.py loaddata servicios/fixtures/servicios_iniciales.json
```

### 5. Crear un superusuario para el panel de administración
```bash
python manage.py createsuperuser
```

### 6. Arrancar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre el navegador en: http://127.0.0.1:8000

Panel de administración: http://127.0.0.1:8000/admin

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
