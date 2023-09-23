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
                            {% include 'right-artist-info.html' %}
                        </div>
                        <div class="right-artist-like-tracks"></div>
                        <div class="right-artist-following"></div>
                        <div class="right-artist-last-comments"></div>
                        <div class="right-artist-another-info"></div>
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


export default {
    name: "MainLayout",    
    components: {
        HeaderNavbar,  
        ModalLoginForm,
        ArtistHeader,
        ModalArtistAvatar,
        FooterPlayer, 
        ContentNavbar,       
        RouterView,
        
    },  
}

</script>