<?php

namespace App\Models\GameNight;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MiscSettings extends Model
{
    const TABLE = 'MiscSettings';

    const FIELD_KEY = 'Key';
    const FIELD_VALUE = 'Value';

    protected $fillable = [
        self::FIELD_KEY,
        self::FIELD_VALUE
    ];

    protected $connection = 'gamenight';
    protected $table = self::TABLE;

    public $timestamps = false;
    
}
