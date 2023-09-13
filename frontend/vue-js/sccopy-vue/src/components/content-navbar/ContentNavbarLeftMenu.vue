<template>
<div class="navbar-content-left">
    <div class="navbar-content-left-link">  
        <RouterLink  
            @click.prevent
            :to="{ name: 'artist-all', params: {artist: 'vasja'}}"
            :class="[activeLink.isActivateAllLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"                      
        >
        All 
        </RouterLink>
    </div>
    <div class="navbar-content-left-link">
        <RouterLink
            @click.prevent 
            :to="{ name: 'artist-popular-tracks', params: {artist: 'vasja'}}"
            :class="[activeLink.isActivatePopularTracksLink.status ? 'navbar-content-left-link-a-active' : '']" 
            class="navbar-content-left-link-a"
        >
        Popular tracks
        </RouterLink>
    </div>
    <div class="navbar-content-left-link">                
        <RouterLink     
            @click.prevent     
            :to="{ name: 'artist-tracks', params: {artist: 'vasja'}}" 
            :class="[activeLink.isActivateTracksLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Tracks
        </RouterLink>
    </div>
    <div class="navbar-content-left-link">                
        <RouterLink
            @click.prevent 
            :to="{ name: 'artist-albums', params: {artist: 'vasja'}}"
            :class="[activeLink.isActivateAlbumsLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Albums
        </RouterLink>
    </div>
    <div class="navbar-content-left-link">                
        <RouterLink
            @click.prevent
            :to="{ name: 'artist-sets', params: {artist: 'vasja'}}"
            :class="[activeLink.isActivatePlaylistsLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Playlists
        </RouterLink>
    </div>
    <div class="navbar-content-left-link">                
        <RouterLink
            @click.prevent
            :to="{ name: 'artist-reposts', params: {artist: 'vasja'}}"
            :class="[activeLink.isActivateRepostsLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Reposts
        </RouterLink>
    </div>
</div>

</template>

<script>

import { RouterLink } from 'vue-router'

export default {
    name: "ContentNavbarLeftMenu",
    components: { 
        RouterLink, 
    },
    data() {
        return {     
            activeLink: {       
                isActivateAllLink: { status: false, name: 'artist-all' },
                isActivatePopularTracksLink: { status: false , name: 'artist-popular-tracks' },
                isActivateTracksLink: { status: false , name: 'artist-tracks' },
                isActivateAlbumsLink: { status: false , name: 'artist-albums' },
                isActivatePlaylistsLink: { status: false , name: 'artist-sets' },
                isActivateRepostsLink: { status: false , name: 'artist-reposts' }, 
            },                                
        }
    },         
       
    watch: {
        '$route.name': {            
            handler() {
                console.log("update route: ", this.$route.name)                
                this.activateLink(this.$route.name)
            },
        }
    },

    methods: { 
        activateLink(routeName) {
            for (let key in this.activeLink) {                 
                if (routeName === this.activeLink[key].name)  {
                    this.activeLink[key].status = true
                }
                else {
                    this.activeLink[key].status = false
                }                 
            }    
        },
    },
    
}

</script>



<style>

.navbar-content-left {
    display: flex;
}

.navbar-content-left-link {
    height: 35px;
    margin-top: 3px;    
}   

.navbar-content-left-link-a {
    margin-right: 25px;    
    cursor: pointer;
    color: #000;
    font-weight: 100;
    text-align: center;
    font-size: 18px;
    line-height: 1.8;  
    pointer-events:stroke;     
}

.navbar-content-left-link-a-active {
    color:#fe5621;
    border-bottom: 2px solid #fe5621;
    cursor: default;
    pointer-events: none;
}

.navbar-content-left-link-a:hover {
    color: #000;    
    border-bottom: 2px solid #000;
}

.navbar-content-left-link-a-active:hover {
    color:#fe5621;
    border-bottom: 2px solid #fe5621;    
}

</style>