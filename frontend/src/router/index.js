import { createRouter, createWebHistory } from "vue-router";
import RegisterPage from "@/views/RegisterPage.vue";
import VerifyPage from "@/views/VerifyPage.vue";
import LoginPage from "@/views/LoginPage.vue";
import AdminPanel from "@/views/AdminPanel.vue";

const routes = [
  { path: "/", component: RegisterPage },
  { path: "/verify", component: VerifyPage },
  { path: "/login", component: LoginPage },
  { 
    path: "/admin", 
    component: AdminPanel, 
    meta: { requiresAuth: true } // Indica que esta ruta requiere autenticación
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Middleware para proteger rutas
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem("accessToken");
    if (!token) {
      // Si no hay token, redirige al inicio de sesión
      next("/login");
    } else {
      next(); // Permite el acceso si hay un token
    }
  } else {
    next(); // Para rutas públicas, continúa sin restricciones
  }
});

export default router;
