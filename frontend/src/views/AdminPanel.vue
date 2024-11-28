<template>
  <div>
    <!-- Pantalla de protección por contraseña -->
    <div class="acceso" v-if="!isAuthenticated">
      <h1>Acceso Administrador</h1>
      <p>Introduce la contraseña para acceder al área de administración:</p>
      <form @submit.prevent="authenticate">
        <input
          v-model="password"
          type="password"
          placeholder="Contraseña"
          required
          autofocus
        />
        <button type="submit">Acceder</button>
      </form>
    </div>

    <!-- Vista de administración -->
    <div v-else>
      <h1>Administrar Sorteo</h1>
      <button @click="generateWinner">Generar Ganador</button>
      <button @click="logout">Cerrar Sesión</button>

      <!-- Mostrar el ganador en grande -->
      <div v-if="winner" class="winner-display">
        <h2>¡Felicidades!</h2>
        <p class="winner-name">{{ winner }}</p> <!-- Muestra el ganador -->
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/axios";

export default {
  name: "AdminPanel",
  data() {
    return {
      password: "",
      isAuthenticated: false, // Variable para saber si el usuario está autenticado
      winner: null, // Almacena el nombre o el email del ganador
    };
  },
  methods: {
    // Método para autenticar con la contraseña
    authenticate() {
      if (this.password === "admin") {
        this.isAuthenticated = true; // Si la contraseña es correcta, se permite el acceso
      } else {
        alert("Contraseña incorrecta. Acceso denegado.");
      }
    },

    // Método para generar el ganador
    async generateWinner() {
      try {
        const response = await api.get("/generate-winner/");
        alert(response.data.message);
        this.winner = response.data.message; // Almacena el ganador en el estado
      } catch (error) {
        const errorMessage = error.response?.data?.error || "Error desconocido";
        alert("Error al generar ganador: " + errorMessage);
      }
    },

    // Método para cerrar sesión
    logout() {
      this.isAuthenticated = false; // Desautentica al usuario
      this.password = ""; // Limpia la contraseña
      this.winner = null; // Limpia el ganador
      alert("Has cerrado sesión.");
    },
  },
};
</script>

<style scoped>
/* Estilos básicos */
.acceso {
  margin-top: 20px;
  text-align: center;
}

form {
  max-width: 400px;
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
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
}

button:hover {
  background-color: #c82333;
}

/* Estilos para la vista de administración */
h1 {
  text-align: center;
}

button {
  margin: 10px 0;
}

/* Estilo para mostrar al ganador */
.winner-display {
  text-align: center;
  margin-top: 30px;
  padding: 20px;
  background-color: #f8d7da;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.winner-name {
  font-size: 3rem;
  font-weight: bold;
  color: #dc3545;
}
</style>
