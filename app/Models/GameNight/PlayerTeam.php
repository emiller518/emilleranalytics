<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class PlayerTeam extends Model
{
    const TABLE = 'PlayerTeam';

    const FIELD_PLAYER_TEAM_ID = 'PlayerTeamID';
    const FIELD_PLAYER_ID = 'PlayerID';

    protected $fillable = [
        self::FIELD_PLAYER_TEAM_ID,
        self::FIELD_PLAYER_ID

    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    public $timestamps = false;

//
//    function Player(): HasMany {
//        return $this->hasMany(Player::class, Player::FIELD_TEAM_GUID, self::FIELD_GUID);
//    }

}
