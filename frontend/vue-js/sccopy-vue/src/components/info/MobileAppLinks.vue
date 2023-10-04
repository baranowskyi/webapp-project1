<template>   

    <span class="text">Go mobile</span>
    <span class="line"></span>
    <div class="app-mobile">
        <a><img class="img-app" src="@/assets/media/mobile-app/appstore.png"></a>
        <a><img src="@/assets/media/mobile-app/googleplay.png"></a>
    </div>

</template>

<style scoped>

.text {
    margin-bottom: 5px;
    display: flex;
}

.line {
    border-top: 1px solid #f2f2f2;    
    display: flex;     
    margin-bottom: 20px;    
}

.app-mobile {
    display: flex;
}

.img-app {
    margin-right: 10px;
    margin-bottom: 20px;
}

a:hover {
    cursor: pointer;
}

</style>