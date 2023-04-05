<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Map extends Model
{
    const TABLE = 'Map';

    const FIELD_MAP_ID = 'MapID';
    const FIELD_GAME_ID = 'GameID';
    const FIELD_NAME = 'Name';
    const FIELD_SIZE = 'Size';

    protected $fillable = [
        self::FIELD_GAME_ID,
        self::FIELD_NAME,
        self::FIELD_SIZE
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_MAP_ID;
    public $incrementing = true;

    public $timestamps = false;

}
