<?php

namespace App\Models\EMillerAnalytics;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class PortfolioPost extends Model
{
    const TABLE = 'PortfolioPost';
    
    const FIELD_PORTFOLIO_POST_ID = 'PortfolioPostID';
    const FIELD_TITLE = 'Title';
    const FIELD_SLUG = 'Slug';
    const FIELD_UPDATED_ON = 'UpdatedOn';
    const FIELD_CONTENT = 'Content';
    const FIELD_CREATED_ON = 'CreatedOn';
    const FIELD_SUB_HEADER = 'SubHeader';
    const FIELD_IMAGE = 'Image';
    const FIELD_HOME_HEADER = 'HomeHeader';
    const FIELD_IMAGE_HEADER = 'ImageHeader';
    const FIELD_PAGE_HEADER = 'PageHeader';
    const FIELD_SCRIPT = 'Script';
    const FIELD_HIDDEN = 'Hidden';
    const FIELD_FEATURED = 'Featured';

    protected $fillable = [
        self::FIELD_TITLE,
        self::FIELD_SLUG,
        self::FIELD_UPDATED_ON,
        self::FIELD_CONTENT,
        self::FIELD_CREATED_ON,
        self::FIELD_SUB_HEADER,
        self::FIELD_IMAGE,
        self::FIELD_HOME_HEADER,
        self::FIELD_IMAGE_HEADER,
        self::FIELD_PAGE_HEADER,
        self::FIELD_SCRIPT,
        self::FIELD_HIDDEN,
        self::FIELD_FEATURED
    ];

    protected $connection = 'emilleranalytics';
    protected $table = self::TABLE;

    protected $primaryKey = self::FIELD_PORTFOLIO_POST_ID;
    public $incrementing = true;

    public $timestamps = false;

}
