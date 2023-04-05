<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class GameMode extends Model
{
    const TABLE = 'GameMode';

    const FIELD_GAME_MODE_ID = 'GameModeID';
    const FIELD_GAME_ID = 'GameID';
    const FIELD_NAME = 'Name';

    protected $fillable = [
        self::FIELD_GAME_ID,
        self::FIELD_NAME,
    ];
    
    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_GAME_MODE_ID;
    public $incrementing = true;

    public $timestamps = false;

//
//    function Player(): HasMany {
//        return $this->hasMany(Player::class, Player::FIELD_TEAM_GUID, self::FIELD_GUID);
//    }

}
