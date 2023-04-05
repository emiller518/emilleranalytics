<?php

namespace App\Repositories\GameNight;

use App\Models\GameNight\Game;
use App\Models\GameNight\GameAccolade;
use App\Models\GameNight\GameMode;
use App\Models\GameNight\GameModeSetting;
use App\Models\GameNight\GameModeStat;
use App\Models\GameNight\Map;
use App\Models\GameNight\MiscSettings;
use App\Models\GameNight\Player;
use App\Models\GameNight\PlayerTeam;
use App\Models\GameNight\MatchInstance;
use App\Models\GameNight\MatchSettings;
use App\Models\GameNight\MatchStats;
use App\Models\GameNight\MatchTeamStats;
use App\Models\GameNight\MatchAccolade;
use App\Models\GameNight\Team;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class GameRepository
{
    public function getAllGames()
    {
        return Game::query()
            ->orderBy(Game::FIELD_NAME, 'ASC')
            ->get();
    }
    public function getAllPlayers()
    {
        return Player::query()
            ->where(Player::FIELD_HIDDEN, '=', '0')
            ->orderByRaw('Rando asc, UPPER('.Player::FIELD_USERNAME.') ASC')
            ->get();
    }

    public function getMiscSettings($value)
    {
        return MiscSettings::query()
            ->where(MiscSettings::FIELD_KEY, '=', $value)
            ->get();
    }

    public function getAllMapsFromGameID($gameID)
    {
        return Map::query()
            ->where(Map::FIELD_GAME_ID, '=', $gameID)
            ->orderBy(Map::FIELD_NAME, 'asc')
            ->get();
    }

    public function getAllAccoladesFromGameID($gameID)
    {
        return GameAccolade::query()
            ->where(GameAccolade::FIELD_GAME_ID, '=', $gameID)
            ->orderBy(GameAccolade::FIELD_NAME, 'asc')
            ->get();
    }

    public function getMatchInfo($matchID)
    {
        return MatchInstance::query()
            ->selectRaw('Match.MatchDate, Match.Video, Game.Name, Map.Name MapName, Match.TeamType, GameMode.Name GMName')
            ->leftJoin('Game', 'Match.GameID', '=', 'Game.GameID')
            ->leftJoin('Map', 'Match.MapID', '=', 'Map.MapID')
            ->leftJoin('GameMode', 'Match.GameModeID', 'GameMode.GameModeID')

            ->where(MatchInstance::FIELD_MATCH_ID, '=', $matchID)
            ->get()[0];
    }

    public function getAllStatColumnsFromGameMode($gameModeID){
        return GameModeStat::query()
            ->select(GameModeStat::FIELD_NAME)
            ->where(GameModeStat::FIELD_GAME_MODE_ID, '=', $gameModeID)
            ->orderBy(GameModeStat::FIELD_GAME_MODE_STAT_ID)
            ->pluck(GameModeStat::FIELD_NAME)
            ->toArray();
    }

    public function getAllStatsFromMatchID($matchID){
        $gameModeID = MatchInstance::query()
            ->select(MatchInstance::FIELD_GAME_MODE_ID)
            ->where(MatchInstance::FIELD_MATCH_ID, '=', $matchID)
            ->get()[0]['GameModeID'];

        $statColumns = $this->getAllStatColumnsFromGameMode($gameModeID);

        $sql = 'MAX(CASE WHEN Key = "Place" THEN Value END) Place, Username Player, ';

        foreach ($statColumns as $stat){
            if($stat == 'Place'){
                $sql = $sql;
            }
            $sql = $sql . "MAX(CASE WHEN Key = '" . $stat . "' THEN Value END) " . $stat . ", ";
        }
        $sql = substr($sql, 0, -2);

        return MatchStats::query()
            ->selectRaw($sql)
            ->leftJoin(Player::TABLE, MatchStats::TABLE . '.' . MatchStats::FIELD_PLAYER_ID, '=', Player::TABLE . '.' . Player::FIELD_PLAYER_ID)
            ->where(MatchStats::FIELD_MATCH_ID, '=', $matchID)
            ->groupBy('Username')
            ->orderBy('Place', 'ASC')
            ->get();
    }

    public function getAllGameModesFromGameID($gameID)
    {
        return GameMode::query()
            ->where(GameMode::FIELD_GAME_ID, '=', $gameID)
            ->get();
    }

    public function getAllTeamsFromGameID($gameID)
    {
        return Team::query()
            ->where(Team::FIELD_GAME_ID, '=', $gameID)
            ->get();
    }

    public function getAllSettingsFromGameModeID($gameModeID)
    {
        return GameModeSetting::query()
            ->where(GameModeSetting::FIELD_GAME_MODE_ID, '=', $gameModeID)
            ->get();
    }


    public function getAllStatsFromGameModeID($gameModeID)
    {
        return GameModeStat::query()
            ->where(GameModeStat::FIELD_GAME_MODE_ID, '=', $gameModeID)
            ->orderBy(GameModeStat::FIELD_GAME_MODE_STAT_ID)
            ->get();
    }

    public function addNewGame($newGame)
    {
        $game = New Game();

        $game->Name = $newGame['Name'];
        $game->ReleaseDate = $newGame['ReleaseDate'];
        $game->MaxPlayers = $newGame['MaxPlayers'];
        $game->PlayersPerConsole = $newGame['PlayersPerConsole'];
        $game->ReleaseType = $newGame['ReleaseType'];
        $game->Genre = $newGame['Genre'];
        $game->BoxArt = $newGame['BoxArt'];

        $game->Save();

        return 'game added successfully';
    }

    public function addNewMap($newMap)
    {
        $map = New Map();

        $map->GameID = $newMap['GameID'];
        $map->Name = $newMap['Name'];
        $map->Size = $newMap['Size'];

        $map->Save();

        return 'map added successfully';
    }

    public function addNewTeam($newTeam)
    {
        $team = New Team();

        $team->Name = $newTeam['Name'];
        $team->GameID = $newTeam['GameID'];
        $team->Color = $newTeam['Color'];

        $team->Save();

        return 'team added successfully';
    }

    public function addNewAccolade($newAccolade)
    {
        $accolade = New GameAccolade();

        $accolade->GameID = $newAccolade['GameID'];
        $accolade->Name = $newAccolade['Name'];
        $accolade->Description = $newAccolade['Description'];

        $accolade->Save();

        return 'accolade added successfully';
    }

    public function addNewPlayer($newPlayer)
    {
        $player = New Player();

        $player->Name = $newPlayer['Name'];
        $player->Username = $newPlayer['Username'];

        $player->Save();

        return 'player added successfully';
    }

    public function addNewGameMode($newGameMode)
    {
        $gameMode = New GameMode();

        $gameMode->GameID = $newGameMode['GameMode']['GameID'];
        $gameMode->Name = $newGameMode['GameMode']['Name'];

        $gameMode->save();

        foreach ($newGameMode['Stats'] as $stat){
            $gameModeStat = New GameModeStat();

            $gameModeStat->GameModeID = $gameMode->GameModeID;
            $gameModeStat->Name = $stat[0];
            $gameModeStat->Type = $stat[1];
            $gameModeStat->Options = $stat[2];
            $gameModeStat->Required = $stat[3];

            $gameModeStat->save();
        }

        if (!empty($newGameMode['Settings'])){
            foreach ($newGameMode['Settings'] as $setting){
                $gameModeSetting = New GameModeSetting();

                $gameModeSetting->GameModeID = $gameMode->GameModeID;
                $gameModeSetting->Name = $setting[0];
                $gameModeSetting->Type = $setting[1];
                $gameModeSetting->Options = $setting[2];
                $gameModeSetting->Required = $setting[3];

                $gameModeSetting->save();
            }
        }

        $message = 'Game Mode ' . $gameMode->GameModeID . ' added successfully.';
        return $message;
    }

    public function teamCheck($players)
    {
        $result = DB::connection('gamenight')
                        ->select("SELECT PlayerTeamID 
                        FROM (SELECT * FROM PlayerTeam order by PlayerID asc)
                        GROUP BY PlayerTeamID
                        HAVING group_concat(PlayerID,',') = '" . $players . "'");

        if($result == []){
            return null;
        }
        else{
            return $result[0]->PlayerTeamID;
        }
    }

    public function getNewPlayerTeamID(){
        // Increment on the largest value in the PlayerTeam table to set the new ID
        return PlayerTeam::max(PlayerTeam::FIELD_PLAYER_TEAM_ID)+1;
    }


    public function addNewMatch($newMatch){
        // Everything from the 'Match' array is basically all we need for the Match table
        $match = New MatchInstance();

        $match->MatchDate = $newMatch['Match']['MatchDate'];
        $match->GameID = $newMatch['Match']['GameID'];
        $match->MapID = $newMatch['Match']['MapID'];
        $match->GameModeID = $newMatch['Match']['GameModeID'];
        $match->TeamType = $newMatch['Match']['TeamType'];
        $match->Duration = $newMatch['Match']['Duration'];
        $match->Video = $newMatch['Match']['Video'];
        $match->Notes = $newMatch['Match']['Notes'];
        // $match->Winner = '1';

        $match->save();

        // If there are settings with this associated game type, loop through them, and log them to the MatchSetting table
        if (!empty($newMatch['Settings'])){
            foreach ($newMatch['Settings'] as $setting){
                $matchSetting = New MatchSettings();

                $matchSetting->MatchID = $match->MatchID;
                $matchSetting->GameModeSettingID = $setting['GameModeSettingID'];
                $matchSetting->Value  = $setting['Value'];

                $matchSetting->save();
            }
        }

        // Loop through every player and their stats in the Stat array
        foreach ($newMatch['Stats'] as $stat){
            // Take the key and value for each stat
            foreach ($stat as $key=>$value)
                // Set the player ID when they Key matches Player
                if($key == 'Player'){
                    $playerID = $value;
                }
                // Otherwise, if there are accolades, we have to process that logic for the Accolade table
                elseif($key == 'Accolades'){
                    if(count($value) > 0){
                        foreach ($value as $accolade){
                            $matchAccolade = New MatchAccolade();

                            $matchAccolade->MatchID = $match->MatchID;
                            $matchAccolade->PlayerID = $playerID;
                            $matchAccolade->GameAccoladeID = $accolade['GameAccoladeID'];
                            $matchAccolade->TimesReceived = $accolade['TimesReceived'];
    
                            $matchAccolade->save();
                        }
                    }
                // Finally, if it's just a regular stat, upload it to the MatchStat table with the given information
                }else{
                    $matchStat = new MatchStats();
                    
                    $matchStat->MatchID = $match->MatchID;
                    $matchStat->PlayerID = $playerID;
                    $matchStat->Key = $key;
                    $matchStat->Value = $value;

                    $matchStat->save();

                    if($key == 'Place' && $value == '1'){
                        $winner = $playerID;
                    }

                }
        }

        // If teams exist
        if ($newMatch['Match']['Teams'] != 0){

            //Loop through the info for each team
            foreach ($newMatch['TeamStats'] as $team){

                // Create a new array for the players, then append players with matching team IDs
                $playerArray = array();
                $teamID = $team['TeamID'];

                // Loop through the player stats to find the team IDs, then append
                foreach ($newMatch['Stats'] as $playerStat){
                    if($playerStat['Team'] == $teamID){
                        array_push($playerArray, $playerStat['Player']);
                    }
                }

                // Sort the array, then convert it from array to string
                sort($playerArray);
                $playerString = implode(',', $playerArray);

                // If the player combo exists, use their ID
                $playerTeamID = $this->teamCheck($playerString);

                // If the player combo does not exist, increment on the max existing team ID
                // Then loop back through the players and add them to the PlayerTeam table
                if(!$playerTeamID){
                    $playerTeamID = $this->getNewPlayerTeamID();

                    foreach ($playerArray as $player){
                        $playerTeam = New PlayerTeam();

                        $playerTeam->PlayerTeamID = $playerTeamID;
                        $playerTeam->PlayerID = $player;

                        $playerTeam->save();
                    }
                }

                // We now have everything we need to add the stats for the team in this for loop.
                // Score and Place are the only two scores we need to keep track of, so create new instances and save them

                $matchTeamScore = new MatchTeamStats();
                $matchTeamPlace = new MatchTeamStats();

                $matchTeamScore->MatchID = $match->MatchID;
                $matchTeamScore->PlayerTeamID = $playerTeamID;
                $matchTeamScore->TeamID = $team['TeamID'];
                $matchTeamScore->Key = 'Score';
                $matchTeamScore->Value = $team['Score'];

                $matchTeamPlace->MatchID = $match->MatchID;
                $matchTeamPlace->PlayerTeamID = $playerTeamID;
                $matchTeamPlace->TeamID = $team['TeamID'];
                $matchTeamPlace->Key = 'Place';
                $matchTeamPlace->Value = $team['Place'];

                if($team['Place'] == 1){
                    $winner = $playerTeamID;
                }

                $matchTeamScore->save();
                $matchTeamPlace->save();
            }
        }

        // Logic to determine if there is a tie (two "Place" key values set to 1).
        // If so, set the winner to 0.
        // If not, we will set the ID of the player or team later

        $firstPlace = 0;

        if($newMatch['Match']['Teams'] == 0){
            foreach($newMatch['Stats'] as $playerStat){
                if ($playerStat['Place'] == 1){
                    $firstPlace++;;
                }
            }
            if ($firstPlace > 1){
                $winner = 0;
            }
        }
        else{
            foreach($newMatch['TeamStats'] as $teamStat){
                if ($teamStat['Place'] == 1){
                    $firstPlace++;;
                }
            }
            if ($firstPlace > 1){
                $winner = 0;
            }
        }

        $match->Winner = $winner;
        $match->save();

        return 'success';
    }
}
