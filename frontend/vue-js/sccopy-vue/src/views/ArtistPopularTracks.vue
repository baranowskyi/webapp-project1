<template>
<div class="artist-popular-tracks left-content-inner">
    <div class="artist-popular-tracks-container">
        <h1>POPULAR TRACKS</h1>
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
 
</template>



<script>

import { artistDisplayNameMixin } from '@/mixins'

export default {
    mixins: [ artistDisplayNameMixin ]
}

</script>



<style>

</style>