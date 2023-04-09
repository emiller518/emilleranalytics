<template>
    <body>
        <div class="container" role="main">

            <div class="text-center header">
                <h1 class="intro">My Blog</h1>
                <hr>
                <span class="caption">A collection of blog posts related to travel, sports, and other experiences over the years</span>
            </div>

            <div class="row blogpost">
                <div class="col-lg-4 blogimg" style="background-image: url('/img/blog/2016nbafinals1.jpg')">
                </div>

                <div class="col-lg-8 blogtext">
                    <h3>Blog Title</h3>
                    <p>Posted on 4/9/2023</p>
                    <p>This is the pagehead! This is what I'm talking about <a href="#"><b>[Read More]</b></a></p>

                    <div class="post-tags">Tags: <a href="#">Tags</a> <a href="#">Coming</a> <a href="#">Soon</a></div>
                </div>
            </div>

            <div class="row blogpost">
                <div class="col-lg-4 blogimg" style="background-image: url('/img/blog/2016nbafinals1.jpg')">
                </div>

                <div class="col-lg-8 blogtext">
                    <h3>Blog Title</h3>
                    <p>Posted on 4/9/2023</p>
                    <p>This is the pagehead! This is what I'm talking about <a href="#"><b>[Read More]</b></a></p>

                    <div class="post-tags">Tags: <a href="#">Tags</a> <a href="#">Coming</a> <a href="#">Soon</a></div>
                </div>
            </div>

            <p style="text-align:left; padding-top:40px; padding-bottom:40px; font-size: 24px; font-weight:300;">
                        <a href="#">&#8592; Newer Posts</a>
                <span style="float:right;">
                        <a href="#">Older Posts &#8594;</a>
                </span>
            </p>

        </div>
    </body>
</template>

<script>
export default {
    name: 'Home',
}
</script>

<style scoped>
.header {
      margin-top: 60px;
      margin-bottom: 90px;
}
.blogpost{
    box-shadow: 0px 15px 45px -9px rgba(0,0,0,.2);
    margin-bottom: 40px;
}

.blogtext{
    padding: 40px;
}

.blogtitle{
    font-size: 1.75rem;
}

.blogimg{
      background-size: cover;
      background-position: center;
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

.intro {
  font-size:80px;
}

span.caption {
    font-size: 27px;
    font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-weight: 300;
}

</style>