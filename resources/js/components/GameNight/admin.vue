<template>
    <div class="p-20">This is game admin page</div>


    <div id="newMatch" class="add-new-main">
        Match Date: <input :disabled="this.disableMatchInfo" type="date" v-model="newMatch.MatchDate"> <br/>

        Game: <select :disabled="this.disableMatchInfo" v-model="newMatch.GameID" 
              @change="getAllDataFromGame(newMatch.GameID)">
                    <option v-for="(items) in this.allGames" :value="items['GameID']">{{ items['Name'] }}</option>
              </select> <br />

        Map: <select :disabled="this.disableMatchInfo" v-model="newMatch.MapID">
                    <option v-for="(items) in this.allMapsFromGameID" :value="items['MapID']">{{ items['Name'] }}</option>
              </select> <br />

        Game Mode: <select :disabled="this.disableMatchInfo" v-model="newMatch.GameModeID" 
                   @change="getAllDataFromGameMode(newMatch.GameModeID)">
                        <option v-for="(items) in this.allGameModesFromGameID" :value="items['GameModeID']">{{ items['Name'] }}</option>
                   </select> <br />

        <div v-if="this.allSettingsFromGameModeID.length > 0 ">Settings: <br/></div>

        <div v-for="(setting, idx) in this.allSettingsFromGameModeID">
            {{ setting['Name'] }}: 
            <input :disabled="this.disableMatchInfo" v-model="this.newMatchSettings[idx].Value" 
                type="number" v-if="setting['Type'] == 'Integer'" >
            <input :disabled="this.disableMatchInfo" v-model="this.newMatchSettings[idx].Value" 
                type="text" v-if="setting['Type'] == 'Text'" >

            <select :disabled="this.disableMatchInfo" v-model="this.newMatchSettings[idx].Value" v-if="setting['Type'] == 'List'">
                    <option v-for="(settingOptions) in setting['Options'].split(',')">{{settingOptions}}</option>
            </select> 
            <br/> 
        </div>

        Number of Players: <input :disabled="this.disableMatchInfo" type="number" v-model="newMatch.Players"> <br/>

        Team Type: <select :disabled="this.disableMatchInfo" v-model="newMatch.TeamType" @change="setTeamLogic">
            <option v-for="(items) in this.allTeamTypes">{{ items['Value'] }}</option>
            </select> <br />

        <div v-if="newMatch.TeamType == 'Multi Team'">
            Number of Teams:
            <input :disabled="this.disableMatchInfo" type="number" v-model="newMatch.Teams" @change="setTeamLogic" min="3">
        </div>

        <div v-if="newMatch.TeamType != 'Free For All'">
            <table>
                <tr>
                    <th>Team</th>
                    <th>Score</th>
                    <th>Place</th>
                </tr>
                <tr v-for="(numTeams) in newMatch.Teams">
                    <td v-if="newTeamMatchStats[numTeams-1]">
                        <select :disabled="this.disableMatchInfo" v-model="newTeamMatchStats[numTeams-1].TeamID">
                            <option v-for="(team) in this.allTeamsFromGameID" :value="team['TeamID']">{{ team['Name'] }}</option>
                        </select>
                    </td>
                    <td v-if="newTeamMatchStats[numTeams-1]">
                        <input :disabled="this.disableMatchInfo" v-model="newTeamMatchStats[numTeams-1].Score">
                    </td>
                    <td v-if="newTeamMatchStats[numTeams-1]">
                        <select :disabled="this.disableMatchInfo" v-model="newTeamMatchStats[numTeams-1].Place">
                            <option v-for="(place) in this.maxPlace">{{ place }}</option>
                        </select>
                    </td>
                </tr>
            </table>
        </div>

        Duration: <input :disabled="this.disableMatchInfo" v-model="newMatch.Duration"> <br/>

        Video: <input :disabled="this.disableMatchInfo" v-model="newMatch.Video"> <br/>

        Notes: <br>
        <textarea :disabled="this.disableMatchInfo" v-model="newMatch.Notes"></textarea>

        <br> <br>

        <button :disabled="this.disableMatchInfo" @click="setMatchStats">Next</button>

        <br> <br> <br>

        <div v-if="this.newMatchStats.length > 0">
            <table>
                <tr>
                    <th v-for="(idx, column) in this.newMatchStats[0]">{{ column }}</th>
                </tr>
                <tr v-for="(idx) in this.newMatchStats.length">

                    <td>
                        <select v-model="this.newMatchStats[idx-1].Player">
                            <option v-for="(player) in this.allPlayers" :value="player['PlayerID']">{{ player['Username'] }}</option>
                        </select>
                    </td>


                    <td v-if="this.newMatch.Teams">
                        <select v-model="this.newMatchStats[idx-1].Team">
                            <option v-for="(team) in this.allTeamsFromGameID" :value="team['TeamID']">{{ team['Name'] }}</option>
                        </select>
                    </td>

                    <td v-if="!this.newMatch.Teams">
                        <select v-model="this.newMatchStats[idx-1].Place">
                            <option v-for="(number) in this.maxPlace">{{ number }}</option>
                        </select>
                    </td>
                    <td v-for="(col) in statsWithoutPlace"><input v-model="this.newMatchStats[idx-1][col.Name]"></td>
                    <td v-if="allAccoladesFromGameID.length > 0">
                        <table>
                            <tr v-if="this.newMatchStats[idx-1]['Accolades'].length > 0">
                                <th>Name</th>
                                <th>Times Received</th>
                            </tr>
                            <tr v-for="(accolade,aind) in this.newMatchStats[idx-1]['Accolades']">
                                <td>
                                    <select v-model="this.newMatchStats[idx-1]['Accolades'][aind]['GameAccoladeID']">
                                        <option v-for="(items) in this.allAccoladesFromGameID" :value="items['GameAccoladeID']">{{ items['Name'] }}</option>
                                    </select>
                                </td>
                                <td>
                                    <input v-model="this.newMatchStats[idx-1]['Accolades'][aind]['TimesReceived']" min="1">
                                </td>
                            </tr>
                        </table>
                        <button @click="addOrRemoveNewPlayerAccolade(idx-1, 'add')">Add</button>
                        <button @click="addOrRemoveNewPlayerAccolade(idx-1, 'remove')">Remove</button>
                    </td>
                </tr>
            </table>
            <br><br>
            <button @click="clearMatchStats">Previous</button>
            <button @click="addNewMatch">Submit</button>
            <br><br>
        </div>

    </div>


     <div>
        <div id="newGame" class="add-new" v-show="show.game">
            <b>add a new game</b> <br/>
            Name: <input v-model="newGame.Name"> <br/>
            Release Date: <input type="date" v-model="newGame.ReleaseDate"> <br/>
            Max Players: <input type="number" v-model="newGame.MaxPlayers"> <br/>
            Players Per Console: <input v-model="newGame.PlayersPerConsole"> <br/>
            Release Type: <input v-model="newGame.ReleaseType"> <br/>
            Genre: <input v-model="newGame.Genre"> <br/>
            Box Art Path: <input v-model="newGame.BoxArt"> <br/>
            <button @click="addNewGame">Submit</button>
        </div>

        <div id="newGameMode" class="add-new" v-show="show.gameMode">
            <b>add a new game mode</b> <br/>
            Game: <select v-model="newGameMode.GameID">
                <option v-for="(items) in this.allGames" :value="items['GameID']">{{ items['Name'] }}</option>
            </select> <br />
            Name: <input v-model="newGameMode.Name"> <br/><br/>

            <b>game mode stats:</b> <br/>
            <table>
                <th>
                    <td>Name</td>
                    <td>Type</td>
                    <td>Options</td>
                    <td>Required</td>
                </th>
                <tr v-for="stat,idx in this.newGameModeStats">
                    <td><input v-model="newGameModeStats[idx][0]"></td>
                    <td>
                        <select v-model="newGameModeStats[idx][1]">
                            <option selected>Integer</option>
                            <option>Text</option>
                            <option>List</option>
                        </select>
                    </td>
                    <td><input v-model="newGameModeStats[idx][2]"></td>
                    <select v-model="newGameModeStats[idx][3]">
                            <option value="1">Yes</option>
                            <option value="0">No</option>
                        </select>
                </tr>
            </table>
            <button @click="addOrRemoveStatColumns('add')">Add New</button>
            <button @click="addOrRemoveStatColumns('remove')">Remove</button>

            <br/> <br/><br/>

            <b>game mode settings (optional):</b> <br/>
            <table>
                <th>
                    <td>Name</td>
                    <td>Type</td>
                    <td>Options</td>
                    <td>Required</td>
                </th>
                <tr v-for="stat,idx in this.newGameModeSettings">
                    <td><input v-model="newGameModeSettings[idx][0]"></td>
                    <td>
                        <select v-model="newGameModeSettings[idx][1]">
                            <option selected>Integer</option>
                            <option>Text</option>
                            <option>List</option>
                        </select>
                    </td>
                    <td><input v-model="newGameModeSettings[idx][2]"></td>
                    <select v-model="newGameModeSettings[idx][3]">
                            <option value="1">Yes</option>
                            <option value="0">No</option>
                        </select>
                </tr>
            </table>
            <button @click="addOrRemoveSettings('add')">Add New</button>
            <button @click="addOrRemoveSettings('remove')">Remove</button>
            <br/><br/>
            <button @click="addNewGameMode()">Submit</button>
        </div>

        <div id="newMap" class="add-new" v-show=show.map>
            <b>game map:</b> <br/>

            Game: <select v-model="newMap.GameID">
                <option v-for="(items) in this.allGames" :value="items['GameID']">{{ items['Name'] }}</option>
            </select> <br />
            Name: <input v-model="newMap.Name"><br/>
            Size: <select v-model="newMap.Size">
                <option>Small</option>
                <option>Medium</option>
                <option>Large</option>
            </select><br/>
            <button @click="addNewMap">Submit</button>
        </div>

        <div id="newAccolade" class="add-new" v-show="show.accolade">
            <b>game accolade:</b> <br/>

            Game: <select v-model="newAccolade.GameID">
                <option v-for="(items) in this.allGames" :value="items['GameID']">{{ items['Name'] }}</option>
            </select> <br />
            Name: <input v-model="newAccolade.Name"><br/>
            Description: <br>
            <textarea v-model="newAccolade.Description"></textarea><br/>
            <button @click="addNewAccolade">Submit</button>
        </div>

        <div id=newPlayer class="add-new" v-show="show.player">
            <b>new player:</b> <br/>
            Username: <input v-model="newPlayer.Username"> <br/>
            Name: <input v-model="newPlayer.Name"> <br/>
            <button @click="addNewPlayer">Submit</button>
        </div>
    </div>

    <div id="newTeam" class="add-new" v-show="show.team">
            <b>new team:</b> <br/>
            
            Name: <input v-model="newTeam.Name"><br/>
            Game:  <select v-model="newTeam.GameID">
                        <option v-for="(items) in this.allGames" :value="items['GameID']">{{ items['Name'] }}</option>
                    </select> <br />
            Color: <input v-model="newTeam.Color"><br/>
            <button @click="addNewTeam">Submit</button>
    </div>


    <div class="showHide">
        <button @click="showAddDiv('game')">Game</button>
        <button @click="showAddDiv('gameMode')">Game Mode</button>
        <button @click="showAddDiv('map')">Map</button>
        <button @click="showAddDiv('accolade')">Accolade</button>
        <button @click="showAddDiv('player')">Player</button>
        <button @click="showAddDiv('team')">Team</button>
        <button @click="log">Log</button>
    </div>

</template>




<script>
import ApiService from "../../services/api/GameNight/api";

export default {
    props: {
    },
    created() {
        this.apiService = ApiService.make();
        
        //load all the existing games
        this.getAllGames();
        this.getAllTeamTypes();
        this.getAllPlayers();
        
    },

    data: function() {
        return {
            apiService: null,
            changeLog: [],

            allGames: {},
            allTeamTypes: [],
            allPlayers: {},

            allMapsFromGameID: {},
            allAccoladesFromGameID: {},
            allGameModesFromGameID: {},
            allTeamsFromGameID: {},
            allSettingsFromGameModeID: {},
            allStatsFromGameModeID: {},

            newGame: {BoxArt: ''},
            newMatch: {Players: 2, MatchDate:"2023-03-12", TeamType: "Free For All", Teams: 0, Duration: '', Notes: '', Video: ''},
            newGameMode: {},
            newGameModeStats: [['Place', 'Integer', '', '1']],
            newGameModeSettings: [],
            newMap: {},
            newTeam: {},
            newAccolade: {},
            newPlayer: {},
            newMatchStats: [],
            newTeamMatchStats: [],
            newMatchSettings: [],
            maxPlace: '',

            show: {game: false, gameMode: false, map: false, accolade: false, player: false, team: false},
            disableMatchInfo: false,
        
        }
    },

    computed: {
        statsWithoutPlace(){
            let swp = this.allStatsFromGameModeID;
            swp = swp.filter((item) => {
                return (item.Name != 'Place')
            })
            return swp;
        },
    },

    methods: {
        showAddDiv(type){
            var condition = this.show[type]
            this.show = {game: false, gameMode: false, map: false, accolade: false, player: false, team: false};
            this.show[type] = !condition;
        },

        getAllMapsFromGameID(gameID){
            this.apiService.getAllMapsFromGameID(gameID).then(
                response => {this.allMapsFromGameID = (response['data']);}
            )
        },

        getAllTeamsFromGameID(gameID){
            this.apiService.getAllTeamsFromGameID(gameID).then(
                response => {this.allTeamsFromGameID = (response['data']);}
            )
        },

        getAllGameModesFromGameID(gameID){
            this.apiService.getAllGameModesFromGameID(gameID).then(
                response => {this.allGameModesFromGameID = (response['data']);}
            )
        },

        getAllAccoladesFromGameID(gameID){
            this.apiService.getAllAccoladesFromGameID(gameID).then(
                response => {this.allAccoladesFromGameID = (response['data']);}
            )
            
        },
        
        getAllSettingsFromGameModeID(gameModeID){
            this.apiService.getAllSettingsFromGameModeID(gameModeID).then(
                response => {this.allSettingsFromGameModeID = (response['data']);
                             this.setNewMatchSettings((response['data']));}
            )
        },

        getAllStatsFromGameModeID(gameModeID){
            this.apiService.getAllStatsFromGameModeID(gameModeID).then(
                response => {this.allStatsFromGameModeID = (response['data']);}
            )
        },

        getAllDataFromGameMode(gameModeID){
            this.getAllStatsFromGameModeID(gameModeID);
            this.getAllSettingsFromGameModeID(gameModeID);
        },

        getAllDataFromGame(gameID){
            this.getAllMapsFromGameID(gameID);
            this.getAllGameModesFromGameID(gameID);
            this.getAllAccoladesFromGameID(gameID);
            this.getAllTeamsFromGameID(gameID);
            this.allSettingsFromGameModeID = {};
            this.newMatchSettings = [];
        },

        setNewMatchSettings(settingArray){
            this.newMatchSettings = [];
            for (let x = 0; x < settingArray.length; x++){
                let setting = {GameModeSettingID: settingArray[x]['GameModeSettingID'], Value: ''};
                this.newMatchSettings.push(setting)
            }
        },

        getAllGames(){
            this.apiService.getAllGames().then(
                response => {this.allGames = response['data']}
            )
        },

        getAllPlayers(){
            this.apiService.getAllPlayers().then(
                response => {this.allPlayers = response['data']}
            )
        },

        getAllTeamTypes(){
            this.apiService.getAllTeamTypes().then(
                response => {this.allTeamTypes = response['data']}
            )
        },

        addNewGame(){
            this.apiService.addNewGame(this.newGame).then(
                response => {console.log(response['data']);}
            )
            this.getAllGames();
            this.show['game'] = false;
        },

        addNewMap(){
            this.apiService.addNewMap(this.newMap).then(
                response => {console.log(response['data']);}
            )
            if(this.newMatch.GameID == this.newMap.GameID){
                this.getAllMapsFromGameID(this.newMap.GameID);
            }
            this.show['map'] = false;
        },

        addNewTeam(){
            this.apiService.addNewTeam(this.newTeam).then(
                response => {console.log(response['data']);}
            )
            if(this.newMatch.GameID == this.newTeam.GameID){
                this.getAllMapsFromGameID(this.newTeam.GameID);
            }
        },

        addNewPlayer(){
            this.apiService.addNewPlayer(this.newPlayer).then(
                response => {console.log(response['data']);}
            )
            this.getAllPlayers();
            this.show['player'] = false;
        },

        addNewAccolade(){
            this.apiService.addNewAccolade(this.newAccolade).then(
                response => {console.log(response['data']);}
            )
            if(this.newMatch.GameID == this.newAccolade.GameID){
                this.getAllAccoladesFromGameID(this.newAccolade.GameID);
            }
        },

        addOrRemoveNewPlayerAccolade(idx, action){
            if(action == 'add'){
                this.newMatchStats[idx]['Accolades'].push({GameAccoladeID: '', TimesReceived: ''});
            }
            else if (action == 'remove'){
                this.newMatchStats[idx]['Accolades'].pop();
            }
        },

        addOrRemoveStatColumns(action){
            if (action == 'add'){
                this.newGameModeStats.push(['','Integer','','1']);
            }
            else if (action == 'remove'){
                this.newGameModeStats.pop();
            }
        },

        addOrRemoveSettings(action){
            if (action == 'add'){
                this.newGameModeSettings.push(['','Integer','','1']);
            }
            else if (action == 'remove'){
                this.newGameModeSettings.pop();
            }
        },

        setTeamLogic(){
            if (this.newMatch.TeamType == 'Free For All'){
                this.newMatch.Teams = 0;
            } 
            else if (this.newMatch.TeamType == 'Two Team'){
                this.newMatch.Teams = 2;
            }
            else if (this.newMatch.TeamType == 'Multi Team' && this.newMatch.Teams < 3){
                this.newMatch.Teams = 3;
            }
            this.setPlaceLogic();
            this.setTeamMatchStats();
        },

        setPlaceLogic(){
            if (this.newMatch.TeamType == 'Free For All'){
                this.maxPlace = this.newMatch.Players;
            }
            else{
                this.maxPlace = this.newMatch.Teams;
            }
        },

        setTeamMatchStats(){
            while (this.newMatch.Teams > this.newTeamMatchStats.length){
                let teamObj = {'TeamID': '', 'Score': '', 'Place': ''};
                this.newTeamMatchStats.push(teamObj);
            }

            while (this.newMatch.Teams < this.newTeamMatchStats.length){
                let teamObj = {'TeamID': '', 'Score': '', 'Place': ''};
                this.newTeamMatchStats.pop(teamObj);
            }
        },

        setMatchStats(){
            this.setPlaceLogic();
            for (let x = 0; x < this.newMatch.Players; x++){
                let matchStats = {Player: ''};
                if (this.newMatch.Teams > 0){
                        matchStats['Team'] = '';
                } 
                else {
                    matchStats['Place'] = x + 1
                }
                for (let i = 0; i < this.statsWithoutPlace.length; i++){
                    matchStats[this.statsWithoutPlace[i]['Name']] = '';
                }
                if (this.allAccoladesFromGameID.length > 0){
                    matchStats['Accolades'] = [];
                }
                this.newMatchStats.push(matchStats);
            }
            this.disableMatchInfo = true;
        },

        clearMatchStats(){
            this.newMatchStats = [];
            this.newTeamMatchStats = [];
            this.disableMatchInfo = false;
        },
        
        addNewGameMode(){
            let gameModeObj = {};

            gameModeObj['GameMode'] = this.newGameMode;
            gameModeObj['Stats'] = this.newGameModeStats;
            gameModeObj['Settings'] = this.newGameModeSettings

            this.apiService.addNewGameMode(gameModeObj).then(
                response => {console.log(response['data']);}
            )
            this.show['gameMode'] = false;
            this.newMatchSettings = [];
        },

        addNewMatch(){
            let matchObj = {}

            matchObj['Match'] = this.newMatch;
            matchObj['Stats'] = this.newMatchStats;
            matchObj['Settings'] = this.newMatchSettings;
            matchObj['TeamStats'] = this.newTeamMatchStats;

            this.apiService.addNewMatch(matchObj).then(
                response => {console.log(response['data']);}
            )
            let date = this.newMatch['MatchDate']

            this.newMatch = {Players: 2, MatchDate: date, TeamType: "Free For All", Teams: 0, Duration: '', Notes: '', Video: ''};
            this.clearMatchStats();

        },

        log(){
            console.log('latest')
            console.log(this.newMatch);
            console.log(this.newMatchStats);
            console.log(this.newMatchSettings);
            console.log(this.newTeamMatchStats);
        }
    }
}

</script>


<style scoped>
.add-new {
    padding: 25px;
    border-style:solid;
    border-width:thin;
}
.success{
    background-color:forestgreen
}
.hidden {
    visibility: hidden;
}
</style>