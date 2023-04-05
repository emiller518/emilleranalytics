<template>
    <h1 class="p-4">Welcome Page from Vue</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/hoops">Hoops</a>
        <a href="/gamenight">Game Night</a>
    </nav>
</template>

<script>
export default {
    name: 'Header',
}
</script>

<style scoped>
    h1 {
        background-color: cornflowerblue;
        color: white;
    }
</style>