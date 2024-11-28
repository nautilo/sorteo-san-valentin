from celery import shared_task
from django.core.mail import send_mail

@shared_task
def enviar_correo(email, asunto, mensaje):
    send_mail(
        asunto,
        mensaje,
        "sorteosanvalentin.test@gmail.com",  # Correo configurado en settings.py
        [email],
    )
@shared_task
def notificar_ganador(email, nombre):
    send_mail(
        "¡Felicidades, ganaste el sorteo!",
        f"Hola {nombre}, has ganado el sorteo de San Valentín. ¡Felicidades!",
        "sorteosanvalentin.test@gmail.com",
        [email],
    )
