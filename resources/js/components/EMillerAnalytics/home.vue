<template>
    <body>

        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel" data-bs-interval="10000">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="/img/home/carousel1.jpg" class="carousel-image" alt="...">

                    <div class="carousel-caption text-center">
                        <h1 class="carousel-caption-header">Ethan Miller</h1>
                        <p class="carousel-caption-secondary">Former Business Analyst - Miami Dolphins</p>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="/img/home/carousel2.jpg" class="carousel-image" alt="...">

                    <div class="carousel-caption text-center">
                        <h1 class="carousel-caption-header">Ethan Miller</h1>
                        <p class="carousel-caption-secondary">Former Men's Basketball Graduate Assistant - College of Saint Rose</p>
                    </div>
                </div>
                <div class="carousel-item" >
                    <img src="/img/home/carousel3.jpg" class="carousel-image" alt="...">
                    
                    <div class="carousel-caption text-center">
                        <h1 class="carousel-caption-header">Ethan Miller</h1>
                        <p class="carousel-caption-secondary">Abbot World Marathon Majors Six Star Finisher</p>
                    </div>
                </div>
            </div>
        </div>

        <section class="pb-5 bg-light" >
            <div class="container">
                <div class="row">

                    <div class="col-xs-12 col-sm-6 col-md-3 toppadding">
                        <div class="text-center">
                            <p><img class="resizeicon" src="/img/home/overview-work.svg" alt="card image"></p>
                            <h4>Experience</h4>
                            <li>Sales & Marketing Business Analyst, Miami Dolphins</li>
                            <li>Data Analyst Intern, Ecolab</li>
                            <li>Men's Basketball Graduate Assistant, Saint Rose</li>
                            <li>Software Developer, American National Insurance</li>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-6 col-md-3 toppadding">
                        <div class="text-center">
                            <p><img class="resizeicon" src="/img/home/overview-education.svg" alt="card image"></p>
                            <h4 class="card-title">Education</h4>
                            <p>
                                M.S. Computer Science <br>
                                    <i>Saint Rose, 2019</i><br>
                                M.S. Business Analytics <br>
                                    <i>Saint Rose, 2018</i><br>
                                B.S. Information Systems <br>
                                    <i>University of Arkansas, 2015</i>
                            </p>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-6 col-md-3 toppadding">
                        <div class="text-center">
                            <p><img class="resizeicon" src="/img/home/overview-running.svg" alt="card image"></p>
                            <h4 class="card-title">World Marathon Majors</h4>
                            <li>Boston 2017 - 4:26:05</li>
                            <li>Chicago 2017 - 3:58:45</li>
                            <li>Tokyo 2018 - 4:54:05</li>
                            <li>Berlin 2018 - 4:09:04</li>
                            <li>London 2019 - 3:59:12</li>
                            <li>NYC 2019 - 4:26:19</li>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-6 col-md-3 toppadding">
                        <div class="text-center">
                            <p><img class="resizeicon" src="/img/home/overview-reading.svg" alt="card image"></p>
                            <h4 class="card-title">As Seen On..</h4>
                            <a href="https://www.news10.com/sports/ethan-millers-inspirational-journey/">ABC News 10 Albany</a><br>
                            <a href="https://www.youtube.com/watch?v=Jv8Jx8dEFAc">1310 The Ticket Dallas</a><br>
                            <a href="https://kotaku.com/the-original-nba-jam-has-been-updated-for-2017-1791310883">Kotaku.com</a><br>
                            <a href="https://www.theverge.com/2017/1/18/14311946/nba-jam-2017-players-rom-hack-lebron-james">TheVerge.com</a><br>
                            <a href="https://www.foxsports.com/nba/gallery/nba-jam-2k17-rosters-update-011817">Foxsports.com</a><br>
                            Facebook Trends
                        </div>
                    </div>

                </div>
            </div>
        </section>

        
        <div class="py-2 toppadding blurbmargins">
            <div class='container-fluid'>
                <div class="row">

                    <div class="col-md-6 align-self-center text-center">
                    <img class="aboutmeimg" src="/img/home/aboutme.jpg" alt="Los Angeles">
                    </div>

                    <div class="col-md-6 align-self-center toppadding btmpadding">
                    <h1 class="display-6 aligncenter">About Me</h1>
                    <p></p>

                    <p>After finishing my undegraduate degree at the University of Arkansas in 2015,
                        I spent a couple of years as a software developer at an insurance company near my hometown. While it paid the bills, it was certainly a far cry from my calling in life.
                        In the fall of 2017 I decided to give up a modest life of software development in the pursuit of a higher education at The College of Saint Rose.
                        Ultimately, I had hoped to land a dream job combining software development and sports, two of my biggest passions.</p>

                        <p>Shortly after graduation, my decision, along with hours upon hours of stalking the Teamwork Online website for new job postings, finally paid off,
                            as I was hired as a Business Analyst with the Miami Dolphins where I currently work.
                        I've absolutely loved the opportunity to contribute to a world class sports organization in my short time on South Beach so far. It's been very cool to
                            get to peek behind the curtains, and to get a chance see the fruits of our labor come to life every Sunday in the fall.
                        </p>

                        <p>In my free time, I enjoy following my favorite sports teams, working on software development projects, and soaking up a bit of Miami sun at the beach.
                        I also train and participate in endurance events for charity, having raised over $35k completing the Abbott World Marathon Majors and Dolphins Cancer Challenge
                            over the last few years.
                        </p>
                    <div class="text-center">
                        <a href="{% url 'aboutme' %}"><button type="button" class="btn btn-secondary text-center">Read More</button></a>
                    </div>

                    </div>
                </div>
            </div>
        </div>

        <div class="album bg-light widemargins">
            <div class="container">
                <h1 class="display-6 aligncenter">
                    <i>Featured Projects</i>
                </h1><br/>
                <div class="row">
                    <div class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top" width="100%" height="200px" src="/img/home/featured1.jpg" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">EMillerAnalytics.com</h5>
                                <p class="card-text">My portfolio and blog built using a Digital Ocean server, Bootstrap, Django, and other languages and frameworks.</p>
                                
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top" width="100%" height="200px" src="/img/home/featured2.jpg" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">NE10 Recap Bot</h5>
                                <p class="card-text">A Python bot that looks at a box score, generates a recap, and posts to a designated Twitter account.</p>
                                
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top" width="100%" height="200px" src="/img/home/featured3.jpg" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">NBA Jam 2k17</h5>
                                <p class="card-text">A modern update of the 1994 SNES classic NBA Jam T.E. featuring updated rosters and much more.</p>
                        
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="py-2 toppadding blurbmargins">
            <div class='container-fluid'>
                <div class="row">

                    <div class="col-md-6 align-self-center toppadding btmpadding">
                        <h1 class="display-6 aligncenter">NCAA DII Basketball</h1>
                        <p>Thanks to Coach Perno, during my time at The College of Saint Rose I was able to contribute to a first class men's basketball program where
                            I served as a graduate assistant for two years.
                        </p>

                        <p>During this time, I was able to not only experience an NCAA tournament win and an exhibition game at the Carrier Dome, a place I'd spent
                            childhood nights rooting on my beloved Syracuse Orange, but I also applied much of what I learned in the classroom writing code and
                            creating pieces of software to benefit the team.
                        </p>

                        <p>Here you will find the results of many of those projects, from various statistics and photos of players around the region, to different models
                        and analysis of players and teams. Though my time with Saint Rose basketball has come to an end, my involvement with the region has not.
                        I currently enjoy spending nights watching the Golden Knights, as well as learning new models and software development techniques utilizing
                        my custom database containing over 10 years of games from around the region.</p>

                        <div class="text-center">
                            <a href="/"><button type="button" class="btn btn-secondary text-center">See More</button></a>
                        </div>
                    </div>
                    <div class="col-md-6 align-self-center text-center">
                        <img class="aboutmeimg" src="/img/home/d2basketball.jpg" alt="Los Angeles">
                    </div>
                </div>
            </div>
        </div>

        <div class="album bg-light widemargins">
            <div class="container">
                <h1 class="display-6 aligncenter">
                    <i>Recent Blog Posts</i>
                </h1><br/>
                <div class="row">
                    <div class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top" width="100%" height="200px" src="/img/blog/2016nbafinals1.jpg" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">Blog Post 1</h5>
                                <p class="card-text">My portfolio and blog built using a Digital Ocean server, Bootstrap, Django, and other languages and frameworks.</p>
                                
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top" width="100%" height="200px" src="/img/home/blog2.png" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">Blog Post 2</h5>
                                <p class="card-text">A Python bot that looks at a box score, generates a recap, and posts to a designated Twitter account.</p>
                                
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top" width="100%" height="200px" src="/img/home/blog3.png" alt="Card image cap">
                            <div class="card-body">
                                <h5 class="card-title">Blog Post 3</h5>
                                <p class="card-text">A modern update of the 1994 SNES classic NBA Jam T.E. featuring updated rosters and much more.</p>
                        
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </body>
</template>


<script>
export default {
  name: 'Home',
}
</script>

<style scoped>
.carousel-image {
  filter: brightness(40%);
  width: 100%;
  height: 500px;
}
.carousel-caption {
    color: white;
    text-align: center;
  top: 50%;
  transform: translateY(-50%);
  bottom: initial;
  display:table-cell;
    vertical-align: middle;
    text-align:center;
}

.carousel-caption-header {
    font-size: 5vw;
    text-shadow: 4px 4px black;
}

.carousel-caption-secondary {
    font-size: 2vw;
    text-shadow: 2px 2px black;
}

.resizeicon{
    width: 30px;
    height: auto;
}

.toppadding {
    padding-top: 25px;
}

.btmpadding {
    padding-bottom: 25px;
}

.aboutmeimg {
    position: relative;
    width: 70%;
}
.aligncenter{
    text-align:center;
}
.widemargins {
    padding-top: 50px;
    padding-bottom: 50px;
}
.blurbmargins {
  margin-left: 60px;
  margin-right: 60px;
}
</style>