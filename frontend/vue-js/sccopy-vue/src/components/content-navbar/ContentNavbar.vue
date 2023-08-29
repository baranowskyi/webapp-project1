<template>
<div class="navbar-content-container">   
    <div class="navbar-content">
        <div class="navbar-content-left">
            <div class="navbar-content-left-link">  
                <RouterLink
                    :to="{ name: 'artist-all', params: {artist: 'vasja'}}"
                    :class="[isActivateAllLink ? 'navbar-content-left-link-a-active' : '']"
                    class="navbar-content-left-link-a"
                >
                All 
                </RouterLink>
            </div>
            <div class="navbar-content-left-link">
                <RouterLink
                    :to="{ name: 'artist-popular-tracks', params: {artist: 'vasja'}}"
                    :class="[isActivatePopularTracksLink ? 'navbar-content-left-link-a-active' : '']" 
                    class="navbar-content-left-link-a"
                >
                Popular tracks
                </RouterLink>
            </div>
            <div class="navbar-content-left-link">                
                <RouterLink                 
                    :to="{ name: 'artist-tracks', params: {artist: 'vasja'}}" 
                    :class="[isActivateTracksLink ? 'navbar-content-left-link-a-active' : '']"
                    class="navbar-content-left-link-a"
                >
                Tracks
                </RouterLink>
            </div>
            <div class="navbar-content-left-link">                
                <RouterLink
                    :to="{ name: 'artist-albums', params: {artist: 'vasja'}}"
                    :class="[isActivateAlbumsLink ? 'navbar-content-left-link-a-active' : '']"
                    class="navbar-content-left-link-a"
                >
                Albums
                </RouterLink>
            </div>
            <div class="navbar-content-left-link">                
                <RouterLink
                    :to="{ name: 'artist-playlists', params: {artist: 'vasja'}}"
                    :class="[isActivatePlaylistsLink ? 'navbar-content-left-link-a-active' : '']"
                    class="navbar-content-left-link-a"
                >
                Playlists
                </RouterLink>
            </div>
            <div class="navbar-content-left-link">                
                <RouterLink
                    :to="{ name: 'artist-reposts', params: {artist: 'vasja'}}"
                    :class="[isActivateRepostsLink ? 'navbar-content-left-link-a-active' : '']"
                    class="navbar-content-left-link-a"
                >
                Reposts
                </RouterLink>
            </div>
        </div>
        <div class="navbar-content-right">  
            <button class="navbar-content-right-button orange-button navbar-content-right-button-insights"><font-awesome-icon icon="fa-solid fa-chart-column" style="color: #fff;" />&nbsp Your Insights</button>          
            <button class="navbar-content-right-button navbar-content-right-button-station"><font-awesome-icon icon="fa-solid fa-tower-cell" />&nbsp Station</button> 
            <button class="navbar-content-right-button navbar-content-right-button-follow orange-button"><font-awesome-icon icon="fa-solid fa-user-plus" style="color: #fff;" />&nbsp Follow</button>           
            <button class="navbar-content-right-button navbar-content-right-button-share"><font-awesome-icon icon="fa-solid fa-share-from-square" />&nbsp Share</button>
            <button class="navbar-content-right-button navbar-content-right-button-edit"><font-awesome-icon icon="fa-solid fa-pen" />&nbsp Edit</button>
            <button class="navbar-content-right-button navbar-content-right-button-letter"><font-awesome-icon icon="fa-solid fa-envelope" /></button>
            <button class="navbar-content-right-button navbar-content-right-button-dots"><font-awesome-icon icon="fa-solid fa-ellipsis" /></button>
        </div>
    </div>
</div> 
</template>

<script>
import router from '@/router'
import { RouterLink } from 'vue-router'

export default {
    name: "ContentNavbar",
    components: { 
        RouterLink, 
    },
    data() {
        return {
            isActivateAllLink: false,
            isActivatePopularTracksLink: false,
            isActivateTracksLink: false,
            isActivateAlbumsLink: false,
            isActivatePlaylistsLink: false,
            isActivateRepostsLink: false,
        };
    },
    methods: {
        
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








.navbar-content-right {
    display: flex;
    right: 0;
    position: absolute;
}

.navbar-content-right-button {    
    margin-left: 5px;
    border: 1px solid #e5e5e5;
    border-radius: 3px;
    background-color: #fff;
    cursor: pointer;
    color: #333;
    white-space: nowrap;
    font-weight: 100;
    text-align: center;
    vertical-align: initial;
    box-sizing: border-box;
    font-size: 14px;
    padding: 5px 10px 5px 10px;   
    line-height: 16px;
}

.orange-button {    
    background: #fe5621 ;
    border: 1px solid #fe5621;
    color: #fff;
}

</style>