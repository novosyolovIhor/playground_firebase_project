<template>
  <div>
    <h2>Welcome to the Dashboard</h2>
    <button @click="logout">Logout</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { signOut } from "firebase/auth";
import { auth } from "../firebase";

export default defineComponent({
  setup() {
    const logout = async () => {
      try {
        await signOut(auth);
        window.location.href = "../Login"; // Redirect to login after logout
      } catch (error) {
        console.error(error);
      }
    };

    return { logout };
  },
});
</script>
