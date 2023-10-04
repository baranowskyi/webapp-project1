<template>
<div class="artist-albums left-content-inner">
    <div class="artist-albums-container">
        <h1>ALBUMS</h1>
        <div class="no-content">
            <img src="@/assets/media/no-content/no-content-artist-albums.png" class="no-content-img">
            <div class="no-content-text-up"></div>
            <div class="no-content-text-down">
                {{ artistDisplayName }} hasn’t created any albums yet.
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