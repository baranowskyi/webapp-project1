<template>
    
    <div class="main">
        <div class="top-header-navbar">
            <HeaderNavbar />
            <ModalLoginForm />                
        </div>
        <div class="content">            
            <RouterView />
        </div>
        <FooterPlayer /> 
    </div>      
          
</template>

<script>

import HeaderNavbar from '@/components/header-navbar/HeaderNavbar.vue'
import ModalLoginForm from '@/components/modal/ModalLoginForm.vue'
import FooterPlayer from '@/components/footer-player/FooterPlayer.vue'


export default {
    name: "EmptyLayout",    
    components: {
        HeaderNavbar,  
        ModalLoginForm,        
        FooterPlayer
    },  
}

</script>

<style scoped>

.content {
    display: table;    
    padding: 0 30px;
    height: 95.5vh;
    width: 1240px;    
    margin: 0 auto;
    background-color: #ffffff;
}
</style>