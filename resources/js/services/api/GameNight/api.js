import axios from 'axios';

export default class ApiService {
    constructor(baseUrl, baseEndpoint, version) {
        this.baseEndpoint = baseEndpoint;
        this.baseUrl = baseUrl;
        this.version = version;
    }

    axios() {
        const axiosConfig = {
            baseURL: `/${this.baseUrl}/v${this.version}/${this.baseEndpoint}`
        }

        return axios.create(axiosConfig);
    }

    static make() {
        return new ApiService('api', 'gamenight', 1);
    }



    getAllGames(){
        return this.axios().get(`/get-all-games`)
    }

    getAllPlayers(){
        return this.axios().get(`/get-all-players`)
    }

    getAllTeamTypes(){
        return this.axios().get(`/get-all-team-types`)
    }

    getAllMapsFromGameID(gameID){
        return this.axios().get(`/get-all-maps/${gameID}`)
    }
    getAllAccoladesFromGameID(gameID){
        return this.axios().get(`/get-all-accolades/${gameID}`)
    }

    getAllGameModesFromGameID(gameID){
        return this.axios().get(`/get-all-game-modes/${gameID}`)
    }

    getAllTeamsFromGameID(gameID){
        return this.axios().get(`/get-all-teams/${gameID}`)
    }

    getMatchInfo(matchID){
        return this.axios().get(`/get-match-info/${matchID}`)
    }
    getAllStatsFromMatchID(matchID){
        return this.axios().get(`/get-all-match-stats/${matchID}`)
    }

    getAllSettingsFromGameModeID(gameModeID){
        return this.axios().get(`/get-all-game-mode-settings/${gameModeID}`)
    }

    getAllStatsFromGameModeID(gameModeID){
        return this.axios().get(`/get-all-game-mode-stats/${gameModeID}`)
    }

    addNewGame(game){
        return this.axios().post(`/add-new-game`, {gameArray: game})
    }
    addNewTeam(team){
        return this.axios().post(`/add-new-team`, {teamArray: team})
    }
    addNewPlayer(player){
        return this.axios().post(`/add-new-player`, {playerArray: player})
    }

    addNewMap(map){
        return this.axios().post(`/add-new-map`, {mapArray: map})
    }

    addNewGameMode(gameMode){
        return this.axios().post(`/add-new-game-mode`, {gameModeArray: gameMode})
    }

    addNewMatch(match){
        return this.axios().post(`/add-new-match`, {matchArray: match})
    }

    addNewAccolade(accolade){
        return this.axios().post(`/add-new-accolade`, {accoladeArray: accolade})
    }

}
