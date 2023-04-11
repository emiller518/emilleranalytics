<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow fixed-top">
        <div class="container">

            <ul class="navbar-nav">
                <li class="nav-item {% if nbar == 'home' %}active{% endif %}">
                    <router-link class="navbar-brand" to="/">Ethan Miller</router-link>
                </li>
            </ul>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse justify-content-end" id="navbarResponsive">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item {% if nbar == 'blog' %}active{% endif %}">
                        <router-link class="nav-link" to="/portfolio">Portfolio</router-link>
                    </li>
                    <li class="nav-item {% if nbar == 'portfolio' %}active{% endif %}">
                        <router-link class="nav-link" to="/blog">Blog</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/gamenight">Game Night</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/d2hoops">D2 Men's Basketball</router-link>
                    </li>
                    <li class="nav-item {% if nbar == 'about' %}active{% endif %}">
                        <router-link class="nav-link" to="/smbeditor">SMB Save Editor</router-link>
                    </li>
                    <li class="nav-item {% if nbar == 'about' %}active{% endif %}">
                        <a class="nav-link" href="#"> Plex</a>
                    </li>
                    <li class="nav-item {% if nbar == 'about' %}active{% endif %}">
                        <router-link class="nav-link" to="/about">About</router-link>
                    </li>
                </ul>
            </div>
            
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Header',
}
</script>

<style scoped>

</style>