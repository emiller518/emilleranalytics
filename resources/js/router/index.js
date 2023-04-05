import {createRouter, createWebHistory } from "vue-router";

import home from "../components/home.vue";

import gamenight_home from "../components/GameNight/home.vue";
import gamenight_about from "../components/GameNight/about.vue";
import gamenight_admin from "../components/GameNight/admin.vue";
import gamenight_match from "../components/GameNight/match.vue";
import gamenight_d3 from "../components/GameNight/d3.vue";

import hoops_home from "../components/Hoops/home.vue";
import hoops_about from "../components/Hoops/about.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: home,
    },
    {
        path: "/gamenight/",
        name: "Game Night - Home",
        component: gamenight_home,
    },
    {
        path: "/gamenight/admin",
        name: "Game Night - Admin",
        component: gamenight_admin,
    },
    {
        path: "/gamenight/about",
        name: "Game Night - About",
        component: gamenight_about,
    },
    {
        path: "/gamenight/match/:id",
        name: "Game Night - Match",
        component: gamenight_match,
    },
    {
        path: "/gamenight/viz",
        name: "Game Night - D3",
        component: gamenight_d3,
    },
    {
        path: "/hoops/about",
        name: "Hoops - About",
        component: hoops_about,
    },
    {
        path: "/hoops/",
        name: "Hoops - Home",
        component: hoops_home,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;