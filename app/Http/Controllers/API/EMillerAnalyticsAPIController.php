<?php

namespace App\Http\Controllers\API;

use App\Factories\JsonAPIResponseFactory;
use App\Repositories\EMillerAnalytics\BlogPostRepository;
use App\Repositories\EMillerAnalytics\PortfolioPostRepository;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Database\Eloquent\Collection;

class EMillerAnalyticsAPIController extends Controller
{
    private $blogPostRepository;
    private $portfolioPostRepository;

    public function __construct(BlogPostRepository $blogPostRepository, PortfolioPostRepository $portfolioPostRepository, Request $request){
        $this->blogPostRepository = $blogPostRepository;
        $this->portfolioPostRepository = $portfolioPostRepository;
        $this->request          = $request;
    }


    public function getAllBlogPosts() {
        return $this->blogPostRepository->getAllBlogPosts();
    }
    public function getAllPortfolioPosts() {
        return $this->portfolioPostRepository->getAllPortfolioPosts();
    }

    public function getBlogPost($slug){
        return $this->blogPostRepository->getBlogPost($slug);
    }

    public function getPortfolioPost($slug){
        return $this->portfolioPostRepository->getPortfolioPost($slug);
    }

}
