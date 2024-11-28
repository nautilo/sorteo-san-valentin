<template>
  <div id="app">
    <!-- Barra de navegación -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
      <div class="container">
        <a class="navbar-brand" href="/">Sorteo San Valentín</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/verify">Verificar cuenta</router-link>
            </li>

            <!-- Registrarse -->
            <li class="nav-item">
              <router-link class="nav-link" to="/">Registrarse</router-link>
            </li>

            <!-- Iniciar sesión -->
            <li class="nav-item">
              <router-link class="nav-link" to="/login">Iniciar sesión</router-link>
            </li>

            <!-- Administrar sorteo, solo si el usuario está logueado y es administrador -->
            <li class="nav-item">
              <router-link class="nav-link" to="/admin">Administrar sorteo</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Contenido principal -->
    <main>
      <router-view /> <!-- Aquí se cargan las vistas -->
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      isLoggedIn: false,  // Verifica si el usuario está logueado
      isAdmin: false,     // Verifica si el usuario es admin
    };
  },
  created() {
    // Verifica si el usuario está logueado y si es admin
    this.isLoggedIn = !!localStorage.getItem("accessToken");
    this.isAdmin = localStorage.getItem("role") === "admin";  // Asumiendo que guardas el rol de admin
  },
};
</script>

<style scoped>
/* Estilos para la navbar */
.navbar {
  background-color: #dc3545;  /* Rojo San Valentín */
  padding: 1rem 2rem;
}

.navbar-brand {
  font-family: 'Brush Script MT', cursive;
  font-size: 1.8rem;
  color: #fff !important;
}

.nav-link {
  color: #fff !important;
  font-size: 1.1rem;
  font-weight: 600;
}

.nav-link:hover {
  color: #f8f9fa !important;
  text-decoration: underline;
}

/* Espaciado y responsive */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
  }

  .navbar-nav .nav-item {
    margin: 0.5rem 0;
  }
}
</style>
