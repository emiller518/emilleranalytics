<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MatchAccolade extends Model
{
    const TABLE = 'MatchAccolade';

    const FIELD_MATCH_ID = 'MatchID';
    const FIELD_PLAYER_ID = 'PlayerID';
    const FIELD_GAME_ACCOLADE_ID = 'GameAccoladeID';
    const FIELD_TIMES_RECEIVED = 'TimesReceived';

    protected $fillable = [
        self::FIELD_MATCH_ID,
        self::FIELD_PLAYER_ID,
        self::FIELD_GAME_ACCOLADE_ID,
        self::FIELD_TIMES_RECEIVED
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    public $timestamps = false;

}
