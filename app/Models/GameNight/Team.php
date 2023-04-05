<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Team extends Model
{
    const TABLE = 'Team';

    const FIELD_TEAM_ID = 'TeamID';
    const FIELD_NAME = 'Name';
    const FIELD_GAME_ID = 'GameID';
    const FIELD_COLOR = 'Color';
    const FIELD_LOGO = 'Logo';

    protected $fillable = [
        self::FIELD_TEAM_ID,
        self::FIELD_NAME,
        self::FIELD_GAME_ID,
        self::FIELD_COLOR,
        self::FIELD_LOGO,
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_TEAM_ID;

    public $timestamps = false;

//
//    function Player(): HasMany {
//        return $this->hasMany(Player::class, Player::FIELD_TEAM_GUID, self::FIELD_GUID);
//    }

}
