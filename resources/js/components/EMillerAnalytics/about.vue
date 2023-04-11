<template>
    <body>
        <div class="x container" role="main">
          <div class="row">
            <div class=" col-lg-12  col-md-12">

              <div class="text-center header">
                <h1 class="intro ">About Me</h1>
                <hr>
              </div>

              <p>
                Welcome to my blog, my name is Ethan Miller, and over the last couple of years it's been my goal to combine my passion for Python development, statistics, and sports into a fulfilling career. I spent the last two years at The College of Saint Rose working on master’s degrees in computer science and business analytics, and also worked with the men’s basketball team as a graduate assistant. 
                Over that time, I've amassed an absurd amount of data from the NE10, CACC, and ECC conferences within the NCAA's Division 2 East Region. 
                Many of these posts will likely be a deeper dive on that data, but some other sports related data and Python projects will likely be touched on as well.
              </p>

              <p>
                In my free time, I've spent the last three years training to complete the World Marathon Majors for various charities with roughly $25,000 raised to date. 
                I'll be wrapping up my 6th and final race this fall as I head back to my home state to take on the New York City Marathon, becoming one of less than 5,000 people in the world to complete each major.
              </p>

              <p class="img-margin text-center">
                <img src="/img/about/aboutme1.jpeg" class="img-padding" alt="Pineapple">
                <img src="/img/about/aboutme2.jpeg" class="img-padding" alt="Pineapple">
              </p>

            <h2 id="professional"><u>Professional</u></h2>
            <div style="height:10px;font-size:10px;">&nbsp;</div>

            <h4 id="saint-rose-mens-basketball---graduate-assistant-2017-19">Saint Rose Men’s Basketball - Graduate Assistant (2017-19)</h4>
            <ul>
              <li>Created scouting reports using a custom excel template and Synergy Software</li>
              <li>Responsible for advanced analytics &amp; logging player +/- on a game and season basis</li>
              <li>Created D2 East Region database for scouting using Python’s BeautifulSoup package and MySQL for advanced research and analysis (as seen on this site)</li>
              <li>Ran <a href="https://www.instagram.com/saintrosembb">@saintrosembb</a> and created content using Adobe Photoshop and Sony Vegas</li>
              <li>Created a scouting report web app using Django and the East Region database for future use</li>
            </ul>

            <h4 id="nalco-water--ecolab---data-analyst-intern-2018">Nalco Water / Ecolab - Data Analyst Intern (2018)</h4>
            <ul>
              <li>Worked with a team of five interns to build software that benefits sales representatives</li>
              <li>Created a model predicting attrition in accounts based on PowerBI data / models</li>
            </ul>

            <h4 id="american-national-insurance---software-developer-2015-17">American National Insurance - Software Developer (2015-17)</h4>
            <ul>
              <li>Created software for insurance lines using Duck Creek Author toolset</li>
              <li>Main developer of Workers Compensation line, deployed in May 2017</li>
            </ul>

            <div style="height:10px;font-size:30px;">&nbsp;</div>

            <h2 id="education"><u>Education</u></h2>
            <div style="height:10px;font-size:10px;">&nbsp;</div>
            <h4 id="the-college-of-saint-rose-class-of-2019">The College of Saint Rose (Class of 2019)</h4>
            <h5 id="master-of-science-business-analytics">Master of Science, Business Analytics</h5>
            <ul>
              <li>Statistics for business analytics</li>
              <li>Predictive modeling using SAS JMP and Knime Software</li>
              <li>Programming with large datasets using Python</li>
              <li>Database theory and design</li>
            </ul>

            <h5 id="master-of-science-information-technology">Master of Science, Information Technology</h5>
            <ul>
              <li>Python programming</li>
              <li>Data structures, algorithm analysis</li>
              <li>Artificial intelligence</li>
              <li>Object oriented programming (Java)</li>
            </ul>

            <h4 id="university-of-arkansas-class-of-2015">University of Arkansas (Class of 2015)</h4>
            <h5 id="bachelor-of-science-information-systems">Bachelor of Science, Information Systems</h5>

            <div style="height:10px;font-size:30px;">&nbsp;</div>

            <p class="img-margin text-center">
              <img src="/img/about/aboutme3.jpg" class="img-padding" alt="Pineapple">
              <img src="/img/about/aboutme4.jpg" class="img-padding" alt="Pineapple">
              <img src="/img/about/aboutme5.jpg" class="img-padding" alt="Pineapple">
            </p>

            <h2 id="personal"><u>Personal</u></h2>
            <div style="height:10px;font-size:10px;">&nbsp;</div>
            <h4 id="world-marathon-majors">World Marathon Majors</h4>
            <ul>
              <li>2017 Boston Marathon (4:26:05) - $5000+ raised, Dana Farber Cancer Institute</li>
              <li>2017 Chicago Marathon (3:58:45) - $2,000 raised, Endure to Cure</li>
              <li>2018 Tokyo Marathon (4:54:05) - $1,000 raised, Family House JP</li>
              <li>2018 Berlin Marathon (4:09:04) - $2,000 raised, Endure to Cure</li>
              <li>2019 London Marathon (3:59:12) - $13,500+ raised, Organization for Autism Research</li>
            </ul>

            <h4 id="nba-jam-2k17-roster-hack">NBA Jam 2k17 Roster Hack</h4>
            <ul>
              <li>Created an updated version of the SNES classic NBA Jam Tournament Edition with current rosters for the 2016-17 season</li>
              <li>117 modern players with correct attributes and appearances, as well as historic players from the original game</li>
              <li>Featured on <a href="https://kotaku.com/the-original-nba-jam-has-been-updated-for-2017-1791310883">Kotaku</a>, <a href="https://www.usatoday.com/story/tech/talkingtech/2017/01/18/how-play-nba-jam-2017-rosters/96728774/">USA Today</a>, <a href="https://www.cbssports.com/nba/news/look-heres-how-you-can-download-play-nba-jam-with-todays-rosters/">CBS Sports</a>, and trending nationally on Facebook</li>
              <li>Download the rom in the links dropdown above!</li>
            </ul>

            <p class="img-spacing text-center">
              <iframe width="480" height="420" src="https://www.youtube.com/embed/s8Oe5c_08-0">
              </iframe>
            </p>


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
.header {
    margin-top: 60px;
    margin-bottom: 90px;
}
.intro {
  font-size:80px;
}
.img-margin{
    margin-top: 50px;
    margin-bottom: 50px;
  }
  .img-padding{
    padding-left:5px;
    padding-right:5px;
  }
</style>