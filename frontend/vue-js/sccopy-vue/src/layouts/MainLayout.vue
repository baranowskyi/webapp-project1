<template>
    
    <div class="main">
        <div class="top-header-navbar">
            <HeaderNavbar />
            <ModalLoginForm />                
        </div>
        <div class="full-content">            
               <ArtistHeader />
               <ModalArtistAvatar />            
            <div class="main-content">                
                <ContentNavbar />
                <div class="main-user-content"> 
                    
                    <div class="left-content">
                        <RouterView /> 
                    </div>
                    
                    <div class="right-content">            
                        <div class="right-artist-info">
                            RIGHT BLOCK
                        </div>
                        <div class="right-artist-like-tracks"></div>
                        <div class="right-artist-following"></div>
                        <div class="right-artist-last-comments"></div>
                        <div class="right-artist-another-info"></div>
                        <MobileAppLinks />
                        <FooterInfo />
                    </div>
                </div> 
            </div>
        </div>
        <FooterPlayer /> 
    </div>      
          
</template>

<script>

import { RouterView } from 'vue-router'
import HeaderNavbar from '@/components/header-navbar/HeaderNavbar.vue'
import ModalLoginForm from '@/components/modal/ModalLoginForm.vue'
import ArtistHeader from '@/components/header/ArtistHeader.vue'
import ModalArtistAvatar from '@/components/modal/ModalArtistAvatar.vue'
import ContentNavbar from '@/components/content-navbar/ContentNavbar.vue'
import FooterPlayer from '@/components/footer-player/FooterPlayer.vue'
import FooterInfo from '@/components/info/FooterInfo.vue'
import MobileAppLinks from '@/components/info/MobileAppLinks.vue'


export default {
    name: "MainLayout",    
    components: {
        HeaderNavbar,  
        ModalLoginForm,
        ArtistHeader,
        ModalArtistAvatar,
        FooterPlayer, 
        FooterInfo,
        MobileAppLinks,
        ContentNavbar,       
        RouterView,
        
    },  
}

</script>

<style>

.main-content {
    display: table;    
    padding: 0 30px;
    height: 100vh;
    width: 1240px;
    margin: 0 auto;
    background-color: #ffffff;
}

</style>