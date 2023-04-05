<?php

namespace App\Http\Controllers\API;

use App\Factories\JsonAPIResponseFactory;
use App\Repositories\GameNight\GameRepository;
use App\Repositories\GameNight\MatchRepository;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Database\Eloquent\Collection;

class GameNightAPIController extends Controller
{
    private $gameRepository;
    private $matchRepository;

    public function __construct(GameRepository $gameRepository, MatchRepository $matchRepository, Request $request){
        $this->gameRepository = $gameRepository;
        $this->matchRepository = $matchRepository;
        $this->request          = $request;
    }


    public function getAllGames() {
        return $this->gameRepository->getAllGames();
    }
    public function getAllPlayers() {
        return $this->gameRepository->getAllPlayers();
    }
    public function getAllTeamTypes() {
        return $this->gameRepository->getMiscSettings('TeamType');
    }

    public function addNewGame(){
        $values = $this->request->get('gameArray');
        return $this->gameRepository->addNewGame($values);
    }

    public function addNewMap(){
        $values = $this->request->get('mapArray');
        return $this->gameRepository->addNewMap($values);
    }

    public function addNewTeam(){
        $values = $this->request->get('teamArray');
        return $this->gameRepository->addNewTeam($values);
    }

    public function addNewPlayer(){
        $values = $this->request->get('playerArray');
        return $this->gameRepository->addNewPlayer($values);
    }

    public function addNewAccolade(){
        $values = $this->request->get('accoladeArray');
        return $this->gameRepository->addNewAccolade($values);
    }

    public function addNewGameMode(){
        $values = $this->request->get('gameModeArray');
        return $this->gameRepository->addNewGameMode($values);
    }

    public function addNewMatch(){
        $values = $this->request->get('matchArray');
        return $this->gameRepository->addNewMatch($values);
    }

    public function getAllMapsFromGameID($gameID) {
        return $this->gameRepository->getAllMapsFromGameID($gameID);
    }

    public function getAllTeamsFromGameID($gameID) {
        return $this->gameRepository->getAllTeamsFromGameID($gameID);
    }

    public function getAllAccoladesFromGameID($gameID) {
        return $this->gameRepository->getAllAccoladesFromGameID($gameID);
    }

    public function getAllGameModesFromGameID($gameID) {
        return $this->gameRepository->getAllGameModesFromGameID($gameID);
    }

    public function getAllStatsFromMatchID($matchID) {
        return $this->gameRepository->getAllStatsFromMatchID($matchID);
    }

    public function getMatchInfo($matchID) {
        return $this->gameRepository->getMatchInfo($matchID);
    }

    public function getAllSettingsFromGameModeID($gameModeID) {
        return $this->gameRepository->getAllSettingsFromGameModeID($gameModeID);
    }

    public function getAllStatsFromGameModeID($gameModeID) {
        return $this->gameRepository->getAllStatsFromGameModeID($gameModeID);
    }

}
