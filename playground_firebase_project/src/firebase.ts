import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDCZ2AUiHorZOElqzCiGuEpSMDErhCwOQA",
  authDomain: "ihor-novosyolov-playgrou-1705e.firebaseapp.com",
  projectId: "ihor-novosyolov-playgrou-1705e",
  storageBucket: "ihor-novosyolov-playgrou-1705e.firebasestorage.app",
  messagingSenderId: "117383210416",
  appId: "1:117383210416:web:f7f78d99c2f5adcb41a275",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Export Firebase Authentication instance
export const auth = getAuth(app);
