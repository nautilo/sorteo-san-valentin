<template>
  <div class="container mt-5">
    <!-- Sección de cabecera con tema de San Valentín -->
    <div class="text-center mb-4">
      <img src="@/assets/heart-icon.png" alt="San Valentín" class="img-fluid mb-3" style="max-width: 100px;">
      <h1 class="display-4 text-danger">¡Bienvenido al Sorteo de San Valentín!</h1>
      <p class="lead">Ingresa tus datos para participar y tener la oportunidad de ganar un premio único.</p>
    </div>

    <!-- Formulario de inicio de sesión -->
    <form @submit.prevent="login" class="bg-light p-4 rounded shadow-sm">
      <div class="row">
        <div class="col-md-6 mb-3">
          <label for="email" class="form-label">Correo electrónico</label>
          <input
            id="email"
            v-model="email"
            type="email"
            class="form-control"
            placeholder="Correo electrónico"
            required
          />
        </div>
        <div class="col-md-6 mb-3">
          <label for="password" class="form-label">Contraseña</label>
          <input
            id="password"
            v-model="password"
            type="password"
            class="form-control"
            placeholder="Contraseña"
            required
          />
        </div>

        <div class="col-12 text-center mt-3">
          <button type="submit" class="btn btn-danger btn-lg w-100">Ingresar</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import api from "@/axios";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    async login() {
      if (!this.validateForm()) return; // Validación antes de enviar la solicitud

      try {
        // Realiza la solicitud al backend
        const response = await api.post("/login/", {
          email: this.email,
          password: this.password,
        });

        // Almacena los tokens en localStorage
        const { access, refresh } = response.data;
        localStorage.setItem("accessToken", access);
        localStorage.setItem("refreshToken", refresh);

        alert("Inicio de sesión exitoso.");

        // Redirige al panel de administración
        this.$router.push("/admin");
      } catch (error) {
        // Manejo de errores
        const errorMessage =
          error.response?.data?.error || "Error desconocido. Inténtalo más tarde.";
        alert(`Error al iniciar sesión: ${errorMessage}`);
      }
    },
    validateForm() {
      // Validaciones básicas
      if (!this.email || !this.password) {
        alert("Por favor, completa todos los campos.");
        return false;
      }
      if (!this.isValidEmail(this.email)) {
        alert("Ingresa un correo electrónico válido.");
        return false;
      }
      return true;
    },
    isValidEmail(email) {
      // Verifica si el correo tiene un formato válido
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    },
  },
};
</script>

<style scoped>
/* Estilos generales */
.form-control {
  border-radius: 25px;  /* Bordes redondeados */
  background-color: #f8f9fa;  /* Fondo suave */
}

/* Título y encabezado */
h1 {
  font-family: 'Brush Script MT', cursive;
  color: #dc3545;  /* Rojo San Valentín */
  font-size: 3rem;
}

/* Botón de submit */
.btn-danger {
  background-color: #dc3545 !important;  /* Rojo San Valentín */
  border: none;
  font-weight: bold;
}

/* Estilo de la imagen */
img {
  max-width: 100px;
  opacity: 0.9;
}

.container {
  max-width: 700px;  /* Máximo tamaño */
  margin-top: 40px;
  margin-bottom: 40px;
}

/* Responsividad */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
}
</style>
