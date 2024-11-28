from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from .models import Usuario
from .tasks import enviar_correo, notificar_ganador
import random
import logging

logger = logging.getLogger(__name__)

# Registro de usuarios
class RegisterView(APIView):
    def post(self, request):
        # Obtener los datos del request
        email = request.data.get("email")
        nombre = request.data.get("nombre")
        apellidos = request.data.get("apellidos")
        rut = request.data.get("rut")
        fecha_nacimiento = request.data.get("fecha_nacimiento")
        telefono = request.data.get("telefono")
        direccion = request.data.get("direccion")
        ciudad = request.data.get("ciudad")
        pais = request.data.get("pais")

        # Verificar que el correo y los campos necesarios están presentes
        if not email or not nombre or not apellidos or not rut:
            return Response({"error": "Correo, nombre, apellidos y RUT son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si el correo ya está registrado
        if Usuario.objects.filter(email=email).exists():
            return Response({"error": "El correo ya está registrado"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el nuevo usuario
        usuario = Usuario.objects.create_user(
            username=email,
            email=email,
            nombre=nombre,
            apellidos=apellidos,
            rut=rut,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            direccion=direccion,
            ciudad=ciudad,
            pais=pais,
            is_active=False,  # Cuenta inactiva hasta que se verifique
        )

        # Generar un código de verificación temporal
        verification_code = random.randint(100000, 999999)
        usuario.set_password(str(verification_code))  # El código como una contraseña temporal
        usuario.save()

        # Enviar correo de verificación como tarea asíncrona
        enviar_correo.delay(
            email,
            "Código de Verificación - Sorteo de San Valentín",
            f"Hola {nombre} {apellidos},\n\nTu código de verificación es: {verification_code}\n\n¡Gracias por registrarte! Te pedimos verificar tu correo."
        )

        return Response({"message": "Usuario registrado. Revisa tu correo para obtener el código de verificación."}, status=status.HTTP_201_CREATED)


# Verificación de usuarios y cambio de contraseña
class VerifyView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")
        new_password = request.data.get("new_password")  # Nuevo campo para la contraseña

        # Verificar que email y código estén presentes
        if not email or not code:
            return Response({"error": "Correo y código son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        # Si se está pasando una nueva contraseña, validarla
        if new_password:
            try:
                validate_password(new_password)  # Validar la contraseña con las reglas de Django
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Buscar al usuario por el correo
            usuario = Usuario.objects.get(email=email)

            # Verificar que el código ingresado sea correcto (usamos la contraseña temporal como código)
            if usuario.check_password(code):
                if new_password:
                    # Si el código es correcto y hay una nueva contraseña, actualizamos la contraseña
                    usuario.set_password(new_password)
                    usuario.save()
                    return Response({"message": "Cuenta verificada y contraseña actualizada con éxito."}, status=status.HTTP_200_OK)
                
                # Si no hay nueva contraseña, solo verificamos la cuenta
                usuario.is_active = True
                usuario.is_verified = True
                usuario.save()
                return Response({"message": "Cuenta verificada con éxito. Ahora puedes iniciar sesión."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Código incorrecto."}, status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)


# Inicio de sesión
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Correo y contraseña son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        # Cambiar 'username' por 'email'
        usuario = authenticate(request, username=email, password=password)

        if usuario:
            if usuario.is_active:
                if not usuario.is_verified:
                    return Response({"error": "Cuenta no verificada. Revisa tu correo."}, status=status.HTTP_403_FORBIDDEN)

                refresh = RefreshToken.for_user(usuario)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Cuenta inactiva. Verifica tu correo."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)


# Generación de ganador
class GenerateWinnerView(APIView):
    def get(self, request):
        # Obtiene a los participantes verificados
        participantes = Usuario.objects.filter(is_verified=True)

        # Verifica si hay participantes verificados
        if not participantes.exists():
            return Response({"error": "No hay participantes verificados"}, status=status.HTTP_400_BAD_REQUEST)

        # Elige un ganador al azar
        ganador = random.choice(participantes)

        # Envía el correo al ganador
        send_mail(
            "¡Felicidades, ganaste el sorteo!",
            f"Hola {ganador.nombre} {ganador.apellidos}, has ganado el sorteo de San Valentín. ¡Felicidades!",
            "sorteosanvalentin.test@gmail.com",  # Cambia con tu correo
            [ganador.email],
        )

        # Responde con el ganador
        return Response({"message": f"El ganador es {ganador.email}. Se ha enviado un correo de notificación."}, status=status.HTTP_200_OK)