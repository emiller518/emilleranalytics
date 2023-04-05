<template>
    <div class="p-20">This is game night home</div>
    <button @click="testquery">Load Games</button>
    <div v-for="(items) in this.test">{{ items['Name'] }}</div>
    <button @click="testpost(this.post)"></button>
</template>

<script>
import ApiService from "../../services/api/GameNight/api";

export default {
    props: {
        // 'options': {
            // required: true
        // },
    },
    created() {
        this.apiService = ApiService.make();
    },

    data: function() {
        return {
            apiService: null,
            changeLog: [],
            test: [],
            post: ['Call of Duty: Black Ops', '11/9/2010', 16, 2, 'Retail', 'First Person Shooter']
        }
    },

    computed: {
    },

    methods: {
        testquery(){
            this.apiService.testquery().then(
                response => {this.test = response['data'];}
            )
        },

        testpost(post){
            this.apiService.testpost(post).then(
                response => {console.log(response['data']);}
            )
        }

    }
}

</script>


<style scoped>
div {
    background-color: coral;
    color: white;
}
</style>