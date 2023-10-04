<template>
    <div v-if="!getTracks" class="artist-tracks left-content-inner">
        <div class="artist-tracks-container">            
            <div class="no-content">
                <img src="@/assets/media/no-content/no-content-artist-tracks.png" class="no-content-img">
                <div class="no-content-text-up">
                    Nothing to hear here        
                </div>
                <div class="no-content-text-down">
                    Follow {{ artistDisplayName }} for updates on sounds they share in the future.
                </div>
            </div>
        </div>    
    </div>

    <MainPlayer 
        v-for="(item, index) in getTracks"
        :key="index"
        :tracks="item"
    />
     
</template>
    
    
    
<script>

import { artistDisplayNameMixin } from '@/mixins'

import MainPlayer from '@/components/player/MainPlayer.vue'

export default {
    name: "ArtistTracks",
    components: {
        MainPlayer
    },
    mixins: [ artistDisplayNameMixin ],

    data() {
        return {
            tracks: [],            
        }
    },

    computed: {
        getTracks() {
            return this.$store.getters["tracksArtist/ALL_TRACKS_ARTIST"] 
        }
    },
    mounted() {
        this.$store.dispatch("tracksArtist/GET_TRACKS_ARTIST", this.$route.params.artist)
        
    }

}

</script>



<style>

</style>

