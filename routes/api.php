<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\API\GameNightAPIController;
use App\Http\Controllers\API\D2MBBAPIController;
use App\Http\Controllers\API\EMillerAnalyticsAPIController;
use App\Http\Controllers\API\SMBEditorController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/


Route::prefix('/v1')->group(function() {

    Route::prefix('/gamenight')->controller(GameNightAPIController::class)->group(function(){
        Route::get('/get-all-games', 'getAllGames');
        Route::get('/get-all-players', 'getAllPlayers');
        Route::get('/get-all-team-types', 'getAllTeamTypes');
        Route::get('/get-all-maps/{gameID}', 'getAllMapsFromGameID');
        Route::get('/get-all-accolades/{gameID}', 'getAllAccoladesFromGameID');
        Route::get('/get-all-game-mode-settings/{gameModeID}', 'getAllSettingsFromGameModeID');
        Route::get('/get-all-game-mode-stats/{gameModeID}', 'getAllStatsFromGameModeID');
        Route::get('/get-all-game-modes/{gameID}', 'getAllGameModesFromGameID');
        Route::get('/get-all-teams/{gameID}', 'getAllTeamsFromGameID');
        Route::get('/get-all-match-stats/{matchID}', 'getAllStatsFromMatchID');
        Route::get('/get-match-info/{matchID}', 'getMatchInfo');
        Route::post('/add-new-game', 'addNewGame');
        Route::post('/add-new-map', 'addNewMap');
        Route::post('/add-new-team', 'addNewTeam');
        Route::post('/add-new-player', 'addNewPlayer');
        Route::post('/add-new-game-mode', 'addNewGameMode');
        Route::post('/add-new-match', 'addNewMatch');
        Route::post('/add-new-accolade', 'addNewAccolade');
    });

    Route::prefix('/d2mbb')->controller(D2MBBAPIController::class)->group(function(){
        // logic goes here
    });

    Route::prefix('/emilleranalytics')->controller(EMillerAnalyticsAPIController::class)->group(function(){
        Route::get('/get-all-blog-posts', 'getAllBlogPosts');
        Route::get('/get-all-portfolio-posts', 'getAllPortfolioPosts');
    });

    Route::prefix('/smb')->controller(SMBEditorController::class)->group(function(){
        Route::put('update-stats/{id}', 'updateStats');
        Route::put('update-visuals/{id}', 'updateVisuals');
        Route::get('get-leagues', 'getLeagues');
        Route::get('get-teams/{league}', 'getTeams');
        Route::get('get-players/{team}', 'getPlayers');
    });

});