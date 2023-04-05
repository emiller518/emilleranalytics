<template>
    <get />
    <router-view />
    
</template>

<script>
import get from './components/header.vue'

export default {
    name: 'app',
    components: {
        get,
    },
}
</script>

<style>

</style>