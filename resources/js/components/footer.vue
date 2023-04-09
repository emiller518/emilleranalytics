<template>
    <div class="footer">
        <ul class="footerimages">
            <a href="https://github.com/emiller518"><img class="footericons" height='40' width='40' src="/img/footer/footer-github.svg" alt="card image"></a>
            <a href="https://www.linkedin.com/in/emiller518/"><img class="footericons" height='40' width='40' src="/img/footer/footer-linkedin.svg" alt="card image"></a>
            <a href="https://www.instagram.com/emiller518/"><img class="footericons" height='40' width='40' src="/img/footer/footer-instagram.svg" alt="card image"></a>
            <a href="mailto:ethanamiller2@gmail.com"><img class="footericons" height='40' width='40' src="/img/footer/footer-email.svg" alt="card image"></a>
        </ul>

        <br>
        <div class="text-center btmpadding">© Ethan Miller  •  2023  •  <a href="mailto:ethanamiller2@gmail.com">ethanamiller2@gmail.com</a></div>
    </div>
</template>

<script>
export default {
    name: 'Header',
}
</script>

<style scoped>
    .footericons{
        margin-left: 30px;
        margin-right: 30px;
    }
    
    .footer {
        clear: both;
        padding: 10px;
        background-color: #81818136;
    }

    .footerimages {
   text-align: center;
   padding-top: 40px;
   padding-left: 0px;
}

</style>