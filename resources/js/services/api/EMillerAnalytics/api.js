import axios from 'axios';

export default class ApiService {
    constructor(baseUrl, baseEndpoint, version) {
        this.baseEndpoint = baseEndpoint;
        this.baseUrl = baseUrl;
        this.version = version;
    }

    axios() {
        const axiosConfig = {
            baseURL: `/${this.baseUrl}/v${this.version}/${this.baseEndpoint}`
        }

        return axios.create(axiosConfig);
    }

    static make() {
        return new ApiService('api', 'emilleranalytics', 1);
    }


    getAllBlogPosts(){
        return this.axios().get(`/get-all-blog-posts`)
    }

    getAllPortfolioPosts(){
        return this.axios().get(`/get-all-portfolio-posts`)
    }

    getBlogPostFromSlug(slug){
        return this.axios().get(`/get-blog-post/${slug}`)
    }

    getPortfolioPostFromSlug(slug){
        return this.axios().get(`/get-portfolio-post/${slug}`)
    }

}
