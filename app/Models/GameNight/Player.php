<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Player extends Model
{
    const TABLE = 'Player';

    const FIELD_PLAYER_ID = 'PlayerID';
    const FIELD_USERNAME = 'Username';
    const FIELD_NAME = 'Name';
    const FIELD_IMAGE_PATH = 'ImagePath';
    const FIELD_RANDO = 'Rando';
    const FIELD_HIDDEN = 'Hidden';

    protected $fillable = [
        self::FIELD_USERNAME,
        self::FIELD_NAME,
        self::FIELD_IMAGE_PATH,
        self::FIELD_RANDO,
        self::FIELD_HIDDEN

    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_PLAYER_ID;
    public $incrementing = true;

    public $timestamps = false;

//
//    function Player(): HasMany {
//        return $this->hasMany(Player::class, Player::FIELD_TEAM_GUID, self::FIELD_GUID);
//    }

}
