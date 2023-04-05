<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class GameAccolade extends Model
{
    const TABLE = 'GameAccolade';

    const FIELD_GAME_ACCOLADE_ID = 'GameAccoladeID';
    const FIELD_GAME_ID = 'GameID';
    const FIELD_NAME = 'Name';
    const FIELD_DESCRIPTION = 'Description';

    protected $fillable = [
        self::FIELD_GAME_ID,
        self::FIELD_NAME,
        self::FIELD_DESCRIPTION
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_GAME_ACCOLADE_ID;
    public $incrementing = true;

    public $timestamps = false;

}
