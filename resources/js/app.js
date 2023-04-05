
// require('./bootstrap');

// import {createApp} from 'vue'

// import app from './app.vue'
// import router from './router/index'

// createApp(app)
//             .use(router)
//             .mount("#app")


import { createApp } from "vue";

import app from "./app.vue";
import router from "./router/index";

createApp(app)
    .use(router)
    .mount("#app");
