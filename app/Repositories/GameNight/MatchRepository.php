<?php

namespace App\Repositories\GameNight;

use App\Models\GameNight\Game;
use App\Models\GameNight\GameAccolade;
use App\Models\GameNight\GameMode;
use App\Models\GameNight\GameModeSetting;
use App\Models\GameNight\GameModeStat;
use App\Models\GameNight\MiscSettings;

use Illuminate\Support\Facades\DB;

class MatchRepository
{
    public function getAllGames()
    {
        return Game::query()
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
}
