import {createRouter, createWebHistory } from "vue-router";

import home from "../components/EMillerAnalytics/home.vue";

import portfolio_home from "../components/EMillerAnalytics/portfolio_home.vue";
import portfolio_post from "../components/EMillerAnalytics/portfolio_post.vue";

import blog_home from "../components/EMillerAnalytics/blog_home.vue";
import blog_post from "../components/EMillerAnalytics/blog_post.vue";

import about from "../components/EMillerAnalytics/about.vue";

import smb_editor from "../components/EMillerAnalytics/smb_editor.vue";

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
        path: "/portfolio/",
        name: "Portfolio",
        component: portfolio_home,
    },
    {
        path: "/portfolio/:slug",
        name: "Portfolio Post",
        component: portfolio_post,
    },
    {
        path: "/blog/",
        name: "Blog",
        component: blog_home,
    },
    {
        path: "/blog/:slug",
        name: "Blog Post",
        component: blog_post,
    },
    {
        path: "/about/",
        name: "About Me",
        component: about,
    },
    {
        path: "/smbeditor/",
        name: "Super Mega Baseball Roster Editor",
        component: smb_editor,
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
        path: "/d2hoops/about",
        name: "Hoops - About",
        component: hoops_about,
    },
    {
        path: "/d2hoops/",
        name: "Hoops - Home",
        component: hoops_home,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;