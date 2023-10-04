<template>
    <div class="no-content">
        <img class="no-content-img" src="@/assets/media/no-content/404-oh-no-artist.png"/>
        <span class="no-content-text-up">
            We can’t find that user.
        </span>
        <span class="no-content-text-down">
            A report has been sent to our tech team, and they’re looking into the problem. Please check back in a bit.
        </span>
        <button class="button">I need help</button>
        <FooterInfo />
    </div>

</template>

<script>

import FooterInfo from '@/components/info/FooterInfo.vue'

export default {
    name: 'PageNotFoundArtist',
    components: {
        FooterInfo,
    }
}

</script>

<style scoped>
.no-content {
    display: grid;
    padding-top: 39px;
    text-align: center;
    padding-bottom: 120px;
}

.no-content-img {
    display: block;
    margin: 0 auto;    
}

.no-content-text-up {
    font-size: 28px; 
    margin: 0 auto; 
    margin-top: 50px;
    width: 50%;
}

.no-content-text-down {
    font-size: 18px;    
    color: #999;
    margin: 0 auto;
    margin-top: 10px;
    width: 31%;    
}

.button {
    margin: 0 auto;
    margin-top: 30px;    
    padding: 2px 11px 2px 10px;
    border: 1px solid #e5e5e5;
    border-radius: 3px;
    background-color: #fff;
    cursor: pointer;
    color: #333;
    font-size: 14px;
    line-height: 20px;    
    font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;
    font-weight: 100;
    text-align: center;
}

.button:hover {
    border: 1px solid #c7c7c7;
}

</style>