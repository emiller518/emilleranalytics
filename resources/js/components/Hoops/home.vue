<template>
    <body>
        
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="/img/home/carousel1.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="/img/home/carousel2.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="/img/home/carousel3.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
      </div>

    </body>
</template>

<script>
//importing bootstrap 5
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import * as Bootstrap from 'bootstrap'
//import DemoComponent from "./components/DemoComponent.vue"
 
export default {
  name: 'Home',
 mounted(){
    // var myCarousel = document.querySelector('#myCarousel')
    //    new Bootstrap.Carousel(myCarousel)
 }
}
</script>
<style scoped>
div {
    background-color: coral;
    color: white;
}
</style>