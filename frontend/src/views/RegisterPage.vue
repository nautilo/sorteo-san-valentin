<template>
  <div class="container mt-5">
    <!-- Sección de cabecera con tema de San Valentín -->
    <div class="text-center mb-4">
      <img src="@/assets/heart-icon.png" alt="San Valentín" class="img-fluid mb-3" style="max-width: 100px;">
      <h1 class="display-4 text-danger">¡Participa y gana una estadía romántica!</h1>
      <p class="lead">Regístrate para tener la oportunidad de ganar un increíble premio para el Día de San Valentín.</p>
    </div>

    <!-- Formulario de Registro -->
    <form @submit.prevent="register" class="bg-light p-4 rounded shadow-sm">
      <div class="row">
        <div class="col-md-6 mb-3">
          <label for="email" class="form-label">Correo electrónico</label>
          <input v-model="email" type="email" id="email" class="form-control" placeholder="Correo electrónico" required />
        </div>
        <div class="col-md-6 mb-3">
          <label for="nombre" class="form-label">Nombre</label>
          <input v-model="nombre" type="text" id="nombre" class="form-control" placeholder="Nombre" required />
        </div>
        <div class="col-md-6 mb-3">
          <label for="apellidos" class="form-label">Apellidos</label>
          <input v-model="apellidos" type="text" id="apellidos" class="form-control" placeholder="Apellidos" required />
        </div>
        <div class="col-md-6 mb-3">
          <label for="rut" class="form-label">RUT</label>
          <input v-model="rut" type="text" id="rut" class="form-control" placeholder="RUT" required />
        </div>
        <div class="col-md-6 mb-3">
          <label for="fecha_nacimiento" class="form-label">Fecha de Nacimiento</label>
          <input v-model="fecha_nacimiento" type="date" id="fecha_nacimiento" class="form-control" placeholder="Fecha de Nacimiento" required />
        </div>
        <div class="col-md-6 mb-3">
          <label for="telefono" class="form-label">Teléfono</label>
          <input v-model="telefono" type="tel" id="telefono" class="form-control" placeholder="Teléfono" />
        </div>
        <div class="col-md-6 mb-3">
          <label for="direccion" class="form-label">Dirección</label>
          <input v-model="direccion" type="text" id="direccion" class="form-control" placeholder="Dirección" />
        </div>
        <div class="col-md-6 mb-3">
          <label for="ciudad" class="form-label">Ciudad</label>
          <input v-model="ciudad" type="text" id="ciudad" class="form-control" placeholder="Ciudad" />
        </div>
        <div class="col-md-6 mb-3">
          <label for="pais" class="form-label">País</label>
          <input v-model="pais" type="text" id="pais" class="form-control" placeholder="País" />
        </div>

        <div class="col-12 text-center mt-3">
          <button type="submit" class="btn btn-danger btn-lg w-100">Registrarse</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import api from "@/axios";  // Asegúrate de que estás importando correctamente tu instancia de Axios

export default {
  name: "RegisterPage",
  data() {
    return {
      email: "",
      nombre: "",
      apellidos: "",
      rut: "",
      fecha_nacimiento: "",
      telefono: "",
      direccion: "",
      ciudad: "",
      pais: "",
    };
  },
  methods: {
    async register() {
      try {
        const response = await api.post("/register/", {
          email: this.email,
          nombre: this.nombre,
          apellidos: this.apellidos,
          rut: this.rut,
          fecha_nacimiento: this.fecha_nacimiento,
          telefono: this.telefono,
          direccion: this.direccion,
          ciudad: this.ciudad,
          pais: this.pais,
        });

        alert(response.data.message);
      } catch (error) {
        const errorMessage =
          error.response && error.response.data && error.response.data.error
            ? error.response.data.error
            : "Error desconocido";
        alert(`Error al registrarse: ${errorMessage}`);
      }
    },
  },
};
</script>

<style scoped>
/* Estilos para el formulario */
.form-control {
  border-radius: 25px;  /* Bordes redondeados */
  background-color: #f8f9fa;  /* Fondo suave */
}

/* Título y encabezado */
h1 {
  font-family: 'Brush Script MT', cursive;
  color: #dc3545;  /* Rojo San Valentín */
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
}

/* Responsividad */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
}
</style>
