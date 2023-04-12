<template>
    <body>
        <div class="x container" role="main">

            <div class="text-center header">
                <h1 class="intro ">My Portfolio</h1>
                <hr>
                <span class="caption">Data science, sports analysis, python programming and more</span>
            </div>

            <article v-for="(post) in this.allPortfolioPosts" class="post-preview">
                <div class="row">
                    
                    <div class="col-lg-10">
                        <h2 class="post-title">{{post.Title}}</h2>
                        <h3 class="post-subtitle">{{post.SubHeader}}</h3>
                        <p class="post-date">{{post.CreatedOn}}</p>

                        <p>
                            {{post.PageHeader}}&nbsp;<a href="#"><b>[Read More]</b></a>
                        </p>

                        <div class="post-tags">Tags: <a href="#">Tags</a> <a href="#">Coming</a> <a href="#">Soon</a></div>
                    </div>

                    <div class="col-lg-2">
                        <img v-bind:src="'/img/portfolio/' + post.Image" class="post-img" alt="asdf">
                    </div>

                </div>
            </article>

            <div class="pagelinks">
            <p style="text-align:left; padding-top:40px; padding-bottom:40px; font-size: 24px; font-weight:30;">
                    <a href="#">&#8592; Newer Posts</a>
                <span style="float:right;">
                        <a href="#">Older Posts &#8594;</a>
                </span>
            </p>
            </div>
            
        </div>
    </body>
</template>

<script>
import ApiService from "../../services/api/EMillerAnalytics/api";
export default {
    name: 'Home',
    props: {
    },
    created() {
        this.apiService = ApiService.make();
        this.getAllPortfolioPosts();
        
    },
    data: function() {
        return {
            apiService: null,
            changeLog: [],

            allPortfolioPosts: {},
        }
    },
    
    methods: {
        getAllPortfolioPosts(){
            this.apiService.getAllPortfolioPosts().then(
                response => {this.allPortfolioPosts = response['data']}
            )
        },
    }


}
</script>

<style scoped>
.header {
    margin-top: 60px;
    margin-bottom: 90px;
}
.intro {
  font-size:80px;
}
span.caption {
    font-size: 27px;
    font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-weight: 300;
}
.post-preview{
    border-bottom:1px solid #eee;
    padding-top: 50px;
    padding-bottom: 50px;
}

.post-preview:last-child{
    border-bottom: 0px;
    margin-bottom: 50px;
}
.post-title{
    font-size:36px;
    margin-top:0px;
    font-weight:800;
}
.post-subtitle{
    margin:0;
    font-weight:300;
    margin-bottom:10px;
}
.post-date{
    color:#808080;
    font-size:18px;
    font-style:italic;
    margin: 0 0 10px;
    font-family:'Lora', 'Times New Roman', serif;
}
.post-tags{
    margin-top:10px;
    margin-bottom:0;
    font-size:15px;
    color:#999
}
.post-tags a{
    padding: 0px 5px;
}
.pagelinks{
    padding: 40px;
    margin: 40px;
}
.post-img{
    border-radius: 50%;
    height: 192px;
    width: 192px;
    float: right;
    margin-left: 30px;
}
</style>