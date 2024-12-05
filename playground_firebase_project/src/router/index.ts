import { createRouter, createWebHistory } from "vue-router";
import { auth } from "../firebase";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import Dashboard from "../components/Dashboard.vue";

const routes = [
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/dashboard", component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
//To prevent unauthenticated users from accessing certain pages (e.g., Dashboard):
router.beforeEach((to, from, next) => {
  const user = auth.currentUser;
  if (to.path === "/dashboard" && !user) {
    next("/login"); // Redirect to login if unauthenticated
  } else {
    next();
  }
});

export default router;
