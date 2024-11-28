# sorteo-san-valentin
 Prueba Técnica Fullstack para CTS Turismo
 Solución desarrollada por Matías Cortés Vera
 Correo de contacto: 8lapse@gmail.com

## Descripción
Este proyecto es una aplicación web para un concurso de San Valentín, donde los usuarios pueden registrarse para participar en el sorteo de un premio especial: una estadía de 2 noches con todo pagado para una pareja. El proyecto está dividido en dos partes principales:

### Frontend: Desarrollado con Vue.js, con una interfaz donde los usuarios pueden registrarse, verificar su cuenta, iniciar sesión y participar en el sorteo.

### Backend: Desarrollado con Django y Django Rest Framework. Se encarga del registro de usuarios, verificación por correo electrónico, gestión del concurso, y la generación del ganador.

## Funcionalidades
-Registro de usuario: El usuario se registra proporcionando su correo electrónico y otros detalles personales.

-Verificación de correo electrónico: Se envía un código de verificación al correo del usuario, quien debe introducirlo para activar su cuenta.

-Inicio de sesión: El usuario puede iniciar sesión utilizando su correo electrónico y la contraseña proporcionada al registrarse.

-Generación del ganador: El administrador puede generar un ganador aleatorio entre los participantes verificados.

## Instrucciones
1. Iniciar Redis (si no está corriendo):
En la terminal, ejecuta el siguiente comando para iniciar Redis (asegúrate de tener Redis instalado):
```redis-server```

2. Iniciar Celery (en el directorio backend):
En el directorio backend, ejecuta el siguiente comando para iniciar Celery:
```celery -A backend worker --loglevel=info --pool=solo```

3. Iniciar el Backend (Django):
En el directorio backend, ejecuta:
```python manage.py runserver```

4. Iniciar el Frontend (Vue.js):
En el directorio frontend, ejecuta:
```npm run serve```
Una vez que hayas iniciado el servidor del backend y el frontend, podrás acceder al proyecto en http://localhost:8080/.

## Configuración del Correo Electrónico
Para el envío de correos electrónicos (como el código de verificación y la notificación del ganador), se ha configurado el backend para usar Gmail SMTP:

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "sorteosanvalentin.test@gmail.com" 
EMAIL_HOST_PASSWORD = "nasreqcbndajikko"  


## Función de la Clave para la Vista Protegida
La clave para acceder a la vista protegida de la administración del sorteo es simplemente "admin". Esta clave debe ser ingresada por el administrador para poder acceder a la página de administración y generar el ganador.

NOTA: para ejecutar el backend es necesaria la instalación de las librerías especificadas en backend/requeriments.txt para el ambiente virtual.