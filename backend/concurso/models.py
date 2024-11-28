from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)  # Campo de verificación
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)  # RUT como campo único
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'  # Usar email como campo de autenticación
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'telefono', 'direccion', 'ciudad', 'pais']

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
