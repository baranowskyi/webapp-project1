<template>
<div class="navbar-content-left">
    <div class="navbar-content-left-link">  
        <router-link  
            @click.prevent
            :to="{ name: 'artist-all', params: {artist: getArtistFromRoute }}"
            :class="[activeLink.isActivateAllLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"                      
        >
        All 
        </router-link>
    </div>
    <div class="navbar-content-left-link">
        <router-link
            @click.prevent 
            :to="{ name: 'artist-popular-tracks', params: {artist: getArtistFromRoute }}"
            :class="[activeLink.isActivatePopularTracksLink.status ? 'navbar-content-left-link-a-active' : '']" 
            class="navbar-content-left-link-a"
        >
        Popular tracks
        </router-link>
    </div>
    <div class="navbar-content-left-link">                
        <router-link     
            @click.prevent     
            :to="{ name: 'artist-tracks', params: {artist: getArtistFromRoute }}" 
            :class="[activeLink.isActivateTracksLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Tracks
        </router-link>
    </div>
    <div class="navbar-content-left-link">                
        <router-link
            @click.prevent 
            :to="{ name: 'artist-albums', params: {artist: getArtistFromRoute }}"
            :class="[activeLink.isActivateAlbumsLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Albums
        </router-link>
    </div>
    <div class="navbar-content-left-link">                
        <router-link
            @click.prevent
            :to="{ name: 'artist-sets', params: {artist: getArtistFromRoute }}"
            :class="[activeLink.isActivatePlaylistsLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Playlists
        </router-link>
    </div>
    <div class="navbar-content-left-link">                
        <router-link
            @click.prevent
            :to="{ name: 'artist-reposts', params: {artist: getArtistFromRoute }}"
            :class="[activeLink.isActivateRepostsLink.status ? 'navbar-content-left-link-a-active' : '']"
            class="navbar-content-left-link-a"
        >
        Reposts
        </router-link>
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
            }                                          
        }
    }, 
    
    mounted() {
        this.updateRoute()      
    },
       
    watch: {
        '$route.name': {            
            handler() {
                this.updateRoute()
            },
        }
    },

    computed: {
        getArtistFromRoute() {  
            const getData = this.$store.dispatch('currentArtist/GET_CURRENT_ARTIST_DATA', this.$route.params.artist)            
            if (getData === "400 Bad Request") {
                this.$router.push('artist-not-found')
            }
            else {
                return this.$route.params.artist
            }
            
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
        updateRoute() {
            console.log("name route: ", this.$route.name)  
            console.log("params route: ", this.$route.params.artist)              
            this.activateLink(this.$route.name)

            // set title page
            // const artist = this.$store.getters["currentArtist/DISPLAY_NAME"]
            // document.title =  this.$route.meta.title.replace(/\[artist\]/i, artist)            
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