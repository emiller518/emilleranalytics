<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MatchTeamStats extends Model
{
    const TABLE = 'MatchTeamStats';

    const FIELD_MATCH_ID = 'MatchID';
    const FIELD_PLAYER_TEAM_ID = 'PlayerTeamID';
    const FIELD_TEAM_ID = 'TeamID';
    const FIELD_KEY = 'Key';
    const FIELD_VALUE = 'Value';

    protected $fillable = [
        self::FIELD_MATCH_ID,
        self::FIELD_PLAYER_TEAM_ID,
        self::FIELD_TEAM_ID,
        self::FIELD_KEY,
        self::FIELD_VALUE,
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    public $timestamps = false;

}
