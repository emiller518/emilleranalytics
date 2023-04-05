<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MatchStats extends Model
{
    const TABLE = 'MatchStats';

    const FIELD_MATCH_ID = 'MatchID';
    const FIELD_PLAYER_ID = 'PlayerID';
    const FIELD_KEY = 'Key';
    const FIELD_VALUE = 'Value';

    protected $fillable = [
        self::FIELD_MATCH_ID,
        self::FIELD_PLAYER_ID,
        self::FIELD_KEY,
        self::FIELD_VALUE,
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    public $timestamps = false;

}
