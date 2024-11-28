from django.urls import path
from .views import RegisterView, VerifyView, LoginView, GenerateWinnerView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registro de usuario
    path('verify/', VerifyView.as_view(), name='verify'),  # Verificación del código y cambio de contraseña
    path('login/', LoginView.as_view(), name='login'),  # Inicio de sesión
    path('generate-winner/', GenerateWinnerView.as_view(), name='generate_winner'),  # Generar ganador
]
