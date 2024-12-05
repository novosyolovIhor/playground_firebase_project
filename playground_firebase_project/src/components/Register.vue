<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <label>Email:</label>
      <input v-model="email" type="email" required />
      <label>Password:</label>
      <input v-model="password" type="password" required />
      <button type="submit">Register</button>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";

export default defineComponent({
  setup() {
    const email = ref("");
    const password = ref("");
    const errorMessage = ref("");

    const register = async () => {
      try {
        await createUserWithEmailAndPassword(auth, email.value, password.value);
        alert("Registration successful!");
        // Redirect user (example: to dashboard)
        window.location.href = "../Dashboard";
      } catch (error: any) {
        errorMessage.value = error.message;
      }
    };

    return { email, password, errorMessage, register };
  },
});
</script>
