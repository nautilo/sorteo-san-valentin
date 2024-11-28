<template>
  <div>
    <div class="title"><h1>Verificar Cuenta</h1></div>
    <form @submit.prevent="verify">
      <div>
        <label for="email">Correo electrónico:</label>
        <input v-model="email" type="email" id="email" placeholder="Correo electrónico" required />
      </div>
      <div>
        <label for="code">Código de verificación:</label>
        <input v-model="code" type="text" id="code" placeholder="Código de verificación" required />
      </div>

      <!-- Campo para nueva contraseña, solo aparece si el código es correcto -->
      <div v-if="showPasswordField">
        <label for="newPassword">Nueva Contraseña:</label>
        <input v-model="newPassword" type="password" id="newPassword" placeholder="Nueva contraseña" required />

        <label for="confirmPassword">Confirmar Contraseña:</label>
        <input v-model="confirmPassword" type="password" id="confirmPassword" placeholder="Confirmar contraseña" required />
      </div>

      <button type="submit">{{ showPasswordField ? 'Actualizar Contraseña' : 'Verificar' }}</button>
    </form>
  </div>
</template>

<script>
import api from "@/axios";

export default {
  name: "VerifyPage",
  data() {
    return {
      email: "",
      code: "",
      newPassword: "",  // Almacenará la nueva contraseña
      confirmPassword: "",  // Almacenará la confirmación de la nueva contraseña
      showPasswordField: false,  // Controlará la visibilidad del campo de nueva contraseña
    };
  },
  methods: {
    async verify() {
      if (this.showPasswordField && this.newPassword !== this.confirmPassword) {
        alert("Las contraseñas no coinciden. Por favor, verifícalas.");
        return;
      }

      try {
        const response = await api.post("/verify/", {
          email: this.email,
          code: this.code,
          new_password: this.newPassword || null, // Si hay nueva contraseña, la enviamos
        });

        // Si la verificación fue exitosa, muestra el campo para ingresar la nueva contraseña
        if (response.data.message) {
          alert(response.data.message);
          if (response.data.message.includes("verificada con éxito")) {
            this.showPasswordField = true;  // Muestra el campo de nueva contraseña si la cuenta fue verificada
          }
        }
        
      } catch (error) {
        alert("Error al verificar: " + error.response.data.error);
      }
    },
  },
};
</script>

<style scoped>
.title{
  margin-top: 20px;
  text-align: center;
}
/* Estilos básicos para el formulario */
form {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #dc3545;  /* Rojo San Valentín */
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
}

button:hover {
  background-color: #c82333;
}
</style>
