<?php

namespace App\Repositories\EMillerAnalytics;

use App\Models\EMillerAnalytics\PortfolioPost;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class PortfolioPostRepository
{
    public function getAllPortfolioPosts()
    {
        return PortfolioPost::query()
            ->where(PortfolioPost::FIELD_HIDDEN, '=', '0')
            ->orderBy(PortfolioPost::FIELD_CREATED_ON, 'desc')
            ->get();
    }


}
