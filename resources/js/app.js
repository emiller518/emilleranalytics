
// require('./bootstrap');

// import {createApp} from 'vue'

// import app from './app.vue'
// import router from './router/index'

// createApp(app)
//             .use(router)
//             .mount("#app")


import { createApp } from "vue";

import "../css/main.css"

// Import Bootstrap and BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import "bootstrap"
// import "bootstrap-vue/dist/bootstrap-vue.css";

import app from "./app.vue";
import router from "./router/index";

createApp(app)
    .use(router)
    .mount("#app");
