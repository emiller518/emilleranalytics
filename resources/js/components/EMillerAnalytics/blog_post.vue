<template>

    <header class="blog-post-header"
    :style="{ 'background-size': 'cover', 'background-image': 'linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(/img/blog/' 
                + this.blogPost.Image + ')'}">

        <div class="container text-center headertext">
            <span class="post-intro ">{{ this.blogPost.Title }}</span>
            <hr class="small">
            <span class="post-caption">{{ this.blogPost.SubHeader }}</span>
        </div>

    </header>

    <div class="x container postcontent" v-html="this.blogPost.Content" role="main">
    </div>

</template>

<script>
import ApiService from "../../services/api/EMillerAnalytics/api";

export default {
    created() {
        this.apiService = ApiService.make();
        this.getBlogPostFromSlug();
    },

    data: function() {
        return {
            apiService: null,
            blogPost: '',
            routeParams: '',
        }
    },

    methods: {
        getBlogPostFromSlug(){
            this.apiService.getBlogPostFromSlug(this.$route.params.slug).then(
                response => {this.blogPost = response['data'];}
            )

        }

    }
}

</script>

<style scoped>
.blog-post-header{
    padding-top: 30px;
}
.headertext{
    padding-top: 5%;
    padding-bottom: 5%;
}
.post-intro{
    color: white;
    font-size: 80px;
    text-shadow: 4px 4px #000000;
    font-weight: 600;
}
.post-caption{
    color: white;
    font-size: 27px;
    font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-weight: 400;
    text-shadow: 2px 2px #000000;
}
hr.small {
        margin: 15px auto;
        border-width: 4px;
        border-color: #FFFF;
  }
div.postcontent{
        margin-top:60px;
        margin-bottom:60px;
    }

</style>
