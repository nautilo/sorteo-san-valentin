import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Import Bootstrap and BootstrapVue
import 'bootstrap/dist/css/bootstrap.css'; // Importa los estilos de Bootstrap
import { BootstrapVue3 } from 'bootstrap-vue-3'; // Importa BootstrapVue3

// Crear la aplicación y usar los plugins
createApp(App)
  .use(router)
  .use(BootstrapVue3)  // Usar BootstrapVue3
  .mount('#app');
