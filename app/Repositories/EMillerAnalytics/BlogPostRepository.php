<?php

namespace App\Repositories\EMillerAnalytics;

use App\Models\EMillerAnalytics\BlogPost;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;

class BlogPostRepository
{
    public function getAllBlogPosts()
    {
        return BlogPost::query()
            ->where(BlogPost::FIELD_HIDDEN, '=', '0')
            ->orderBy(BlogPost::FIELD_CREATED_ON, 'desc')
            ->get();
    }

    public function getBlogPost($slug)
    {
        return BlogPost::query()
            ->where(BlogPost::FIELD_SLUG, '=', $slug)
            ->get()[0];
    }


}
