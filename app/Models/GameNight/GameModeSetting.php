<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class GameModeSetting extends Model
{
    const TABLE = 'GameModeSetting';

    const FIELD_GAME_MODE_SETTING_ID = 'GameModeSettingID';
    const FIELD_GAME_MODE_ID = 'GameModeID';
    const FIELD_NAME = 'Name';
    const FIELD_TYPE = 'Type';
    const FIELD_OPTIONS = 'Options';
    const FIELD_REQUIRED = 'Required';

    protected $fillable = [
        self::FIELD_GAME_MODE_ID,
        self::FIELD_NAME,
        self::FIELD_TYPE,
        self::FIELD_OPTIONS,
        self::FIELD_REQUIRED,
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_GAME_MODE_SETTING_ID;
    public $incrementing = true;

    public $timestamps = false;

}
