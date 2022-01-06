import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import "mosha-vue-toastify/dist/style.css";


var cors = require('cors')


createApp(App).use(router,cors).mount('#app')
