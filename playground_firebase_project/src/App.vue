<script setup lang="ts">
import Login from './components/Login.vue'; // Import your Login component
import HelloWorld from './components/HelloWorld.vue'; // Import HelloWorld component if needed
</script>

<template>
  <div id="app">
    <h1>Welcome to My App</h1>
    <!-- Render the Login component -->
    <Login />
    <!-- Optionally include HelloWorld -->
    <HelloWorld msg="Vite + Vue" />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
