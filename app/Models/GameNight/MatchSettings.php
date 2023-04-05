<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MatchSettings extends Model
{
    const TABLE = 'MatchSettings';

    const FIELD_MATCH_ID = 'MatchID';
    const FIELD_GAME_MODE_SETTING_ID = 'GameModeSettingID';
    const FIELD_VALUE = 'Value';

    protected $fillable = [
        self::FIELD_MATCH_ID,
        self::FIELD_GAME_MODE_SETTING_ID,
        self::FIELD_VALUE,
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    public $timestamps = false;

//
//    function Player(): HasMany {
//        return $this->hasMany(Player::class, Player::FIELD_TEAM_GUID, self::FIELD_GUID);
//    }

}
