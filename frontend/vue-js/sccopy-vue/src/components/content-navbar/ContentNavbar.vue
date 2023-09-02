<template>
<div class="navbar-content-container">   
    <div class="navbar-content">
        <ContentNavbarLeftMenu />
        <ContentNavbarRightMenu />        
    </div>
</div> 
</template>

<script>

import ContentNavbarLeftMenu from '@/components/content-navbar/ContentNavbarLeftMenu.vue'
import ContentNavbarRightMenu from '@/components/content-navbar/ContentNavbarRightMenu.vue'

export default {
    name: "ContentNavbar",
    components: {
        ContentNavbarLeftMenu,
        ContentNavbarRightMenu,
    },       
}

</script>

<style>

.navbar-content-container {    
    width: 100%;
    height: 35px;  
    position: relative;
    margin-top: 12px;
    border-bottom: 1px solid #e5e5e5;
}

.navbar-content { 
    display: flex;
}

</style>