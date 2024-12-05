<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <label>Email:</label>
      <input v-model="email" type="email" required />
      
      <label>Password:</label>
      <input v-model="password" type="password" required />
      
      <button type="submit">Login</button>
      
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { auth } from "../firebase"; 
import { signInWithEmailAndPassword } from "firebase/auth";

const email = ref("");
const password = ref("");
const errorMessage = ref("");

const login = async () => {
  try {
    await signInWithEmailAndPassword(auth, email.value, password.value);
    alert("Login successful!");
  } catch (error: any) {
    errorMessage.value = error.message || "Login failed.";
  }
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-align: center;
}

input {
  width: calc(100% - 20px);
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #42b883;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #36a775;
}

.error {
  color: red;
  font-size: 14px;
}
</style>
