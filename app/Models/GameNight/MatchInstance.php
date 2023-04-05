<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MatchInstance extends Model
{
    const TABLE = 'Match';

    const FIELD_MATCH_ID = 'MatchID';
    const FIELD_MATCH_DATE = 'MatchDate';
    const FIELD_GAME_ID = 'GameID';
    const FIELD_MAP_ID = 'MapID';
    const FIELD_GAME_MODE_ID = 'GameModeID';
    const FIELD_TEAM_TYPE = 'TeamType';
    const FIELD_WINNER = 'Winner';
    const FIELD_DURATION = 'Duration';
    const FIELD_VIDEO_PATH = 'VideoPath';
    const FIELD_NOTES = 'Notes';

    protected $fillable = [
        self::FIELD_MATCH_DATE,
        self::FIELD_GAME_ID,
        self::FIELD_MAP_ID,
        self::FIELD_GAME_MODE_ID,
        self::FIELD_TEAM_TYPE,
        self::FIELD_WINNER,
        self::FIELD_NOTES

    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_MATCH_ID;
    public $incrementing = true;

    public $timestamps = false;

//
//    function Player(): HasMany {
//        return $this->hasMany(Player::class, Player::FIELD_TEAM_GUID, self::FIELD_GUID);
//    }

}
