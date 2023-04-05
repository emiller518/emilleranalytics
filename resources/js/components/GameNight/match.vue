<template>

    <br><br><br>

    <div>Date: {{ matchInfo['MatchDate'] }}</div>
    <div>{{ matchInfo['Name'] }}</div>
    <div>{{ matchInfo['TeamType'] }} {{ matchInfo['GMName'] }}</div>
    <div>{{ matchInfo['MapName'] }}</div>

    <br>

    <iframe v-if="matchInfo['Video']" width="560" height="315" :src="matchInfo['Video']" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
    </iframe>

    <br>
    <br>
    <br>

    <table>
        <tr>
            <th v-for="(value, key) in matchStats[0]">{{ key }}</th>
        </tr>
        <tr v-for="(playerStat) in matchStats">
            <td v-for="(stat) in playerStat">{{ stat }} </td>
        </tr>
    </table>
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
        this.getAllStatsFromMatchID();
        this.getMatchInfo();
    },

    data: function() {
        return {
            apiService: null,
            changeLog: [],
            matchStats: [],
            matchInfo: [],
        }
    },

    computed: {
    },

    methods: {
        getAllStatsFromMatchID(){
            this.apiService.getAllStatsFromMatchID(this.$route.params.id).then(
                response => {this.matchStats = response['data'];}
            )
        },

        getMatchInfo(){
            this.apiService.getMatchInfo(this.$route.params.id).then(
                response => {this.matchInfo = response['data'];}
            )
        }

    }
}

</script>


<style scoped>
div {
    /* background-color: coral;
    color: white; */
    color: black;
}
</style>