<template>

<div class="audio-container">

    <!-- track image -->
    <div class="track-img">
        <img class="cover-img" :src="tracks.cover_image">
    </div>

    <!-- track info top -->
    <div class="track-container">
        <div class="track-top-info">
            <span class="main-play-button" @click="playButton()">
                <font-awesome-icon  icon="fa-solid fa-circle-play"/>
                <font-awesome-icon  icon="fa-solid fa-circle-pause"/>
            </span>
            <div class="name-container">
                <div class="name-artist"><a class="name-artist-a" href="#">{{ tracks.artist.display_name }}</a></div>
                <div class="name-track"><a class="name-track-a" href="#">{{ tracks.title }}</a></div>
            </div>
            <div class="date-tag-container">
                <div class="date-track">${publishDateAgo}</div> 
                <div v-if="tracks.genre" class="tag-track"><font-awesome-icon icon="fa-solid fa-hashtag"/>&nbsp {{ tracks.genre }}</div> 
            </div>
        </div>

        <!-- wave form -->
        <div class="waveform" :id="`waveform${tracks.id}`">
            <div class="time" :id="`time${tracks.id}`">0:00</div>
            <div class="duration" :id="`duration${tracks.id}`">0:00</div>
            <div class="hover" :id="`hover${tracks.id}`"></div>
        </div>          

        <!-- track info botton -->
        <div class="track-bottom-container">
            <button class="like-button default-bt"><font-awesome-icon icon="fa-solid fa-heart"/>
                <div class="like-button-text" style="display: contents;">${likeCounter}</div>
            </button>  
            <button class="repost-button default-bt"><font-awesome-icon icon="fa-solid fa-retweet"/>
                <div class="repost-button-text" style="display: contents;">159</div>
            </button>
            <button class="share-button default-bt"><font-awesome-icon icon="fa-solid fa-share-from-square"/>&nbsp Share</button>
            <button class="copy-link-button default-bt"><font-awesome-icon icon="fa-solid fa-link"/>&nbsp Copy Link</button>  
            <button class="edit-button default-bt"><font-awesome-icon icon="fa-solid fa-pen"/>&nbsp Edit</button>        
            <button class="more-button default-bt"><font-awesome-icon icon="fa-solid fa-ellipsis"/>&nbsp More</button> 
            <button class="download-button default-bt"><font-awesome-icon icon="fa-solid fa-download" style="color: #fe5621"/></button>
            <div class="buy-button"><a class="buy-button-a" href="#">Buy</a></div>
            <div class="play-like-repost-bottom">            
                <div class="play-counter"><font-awesome-icon icon="fas fa-play"/>&nbsp 34</div> 
                <div class="repost-counter"><a class="repost-counter-a" href="#"><font-awesome-icon icon="fa-solid fa-retweet"/>&nbsp 2344</a></div>
                <div class="comment-counter"><a class="comment-counter-a" href="#"><font-awesome-icon icon="fa-solid fa-message"/>&nbsp 44</a></div>
            </div>
        </div>
    </div>  
</div>  

</template>

<script>

import WaveSurfer from 'wavesurfer.js'

export default {
    name: "MainPlayer",
    data() {
        return {
            
        }
    },

    props: {
        tracks: {}
    },

    computed: {
        
    },

    mounted() {   
        
        // console.log("PROPS: ", this.tracks.id)

        const canvas = document.createElement('canvas')
        const ctx = canvas.getContext('2d')

        // Define the waveform gradient
        const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height * 1.06)
        gradient.addColorStop(0, '#656666') // Top color
        gradient.addColorStop((canvas.height * 0.33) / canvas.height, '#656666') // Top color
        gradient.addColorStop((canvas.height * 0.33 + 1) / canvas.height, '#ffffff') // White line
        gradient.addColorStop((canvas.height * 0.33 + 2) / canvas.height, '#ffffff') // White line
        gradient.addColorStop((canvas.height * 0.33 + 3) / canvas.height, '#B1B1B1') // Bottom color
        gradient.addColorStop(1, '#B1B1B1') // Bottom color

        // Define the progress gradient
        const progressGradient = ctx.createLinearGradient(0, 0, 0, canvas.height * 1.06)
        progressGradient.addColorStop(0, '#EE772F') // Top color
        progressGradient.addColorStop((canvas.height * 0.33) / canvas.height, '#EB4926') // Top color
        progressGradient.addColorStop((canvas.height * 0.33 + 1) / canvas.height, '#ffffff') // White line
        progressGradient.addColorStop((canvas.height * 0.33 + 2) / canvas.height, '#ffffff') // White line
        progressGradient.addColorStop((canvas.height * 0.33 + 3) / canvas.height, '#F6B094') // Bottom color
        progressGradient.addColorStop(1, '#F6B094') // Bottom color

        this.wavesurfer = WaveSurfer.create({
            container: "#waveform" + this.tracks.id,
            waveColor: gradient,
            progressColor: progressGradient,
            barWidth: 2,
            height: 60,
            url: this.tracks.track_file
        })

        // Hover effect
        const hover = document.querySelector('#hover' + this.tracks.id)
        const waveform = document.querySelector('#waveform' + this.tracks.id)
        waveform.addEventListener('pointermove', (e) => (hover.style.width = `${e.offsetX}px`))

        //************************************** TIME INDICATION ************************************************/
            
        // Current time & duration
        const formatTime = (seconds) => {
            const minutes = Math.floor(seconds / 60)
            const secondsRemainder = Math.round(seconds) % 60
            const paddedSeconds = `0${secondsRemainder}`.slice(-2)
            return `${minutes}:${paddedSeconds}`
        }

        // main player
        const timeEl = document.querySelector('#time' + this.tracks.id)
        const durationEl = document.querySelector('#duration' + this.tracks.id)
        this.wavesurfer.on('decode', (duration) => (durationEl.textContent = formatTime(duration)))
        this.wavesurfer.on('timeupdate', (currentTime) => (timeEl.textContent = formatTime(currentTime)))

        // play/pause on click
        this.wavesurfer.on('interaction', () => { 
            // playMainButton.classList.add("playing")
            // playFooterButton.classList.add("playing")
            // this.wavesurfer.setVolume(checkVolume)
            this.wavesurfer.setVolume(0.2)
            // checkProgressValue = wavesurfer.getCurrentTime()
            // getProgress(checkProgressValue)
            this.wavesurfer.play()
        })
    },
    methods: {
        playButton() {
            // play/pause on main button
            this.wavesurfer.setVolume(0.2)
            this.wavesurfer.playPause()
        },
        isPlayPlayer() {
            return this.wavesurfer.isPlaying()
        }
    }
}

</script>


<style>

/**************************************************************************************************/
/************************************************* PLAYER IN PAGE *********************************/
/**************************************************************************************************/

.audio-container { 
    width: 100%;        
    position: relative;
    display: flex;
    margin-bottom: 35px;
}
  
.audio-container .audio {    
    width: 100%;   
}
  
.buttons {
    position: absolute;
    right: 0;    
}
  
.audio-container .btn {
    padding: 16px;
    width: 24px;
    margin-right: 10px;
    cursor: pointer;
    display: inline-block;
}

/******************************************************************* COVER TRACK ****************************************/

.track-img {
    background: transparent 50%/contain no-repeat;
    display: block;
    height: 160px;
    width: 160px;
    position: relative;
    margin-right: 10px;
}

.cover-img {
    width: 100%;
    height: 100%;
    cursor: pointer;
    background-image: linear-gradient(135deg,#846170,#70929c);
    box-shadow: inset 0 0 0 1px rgba(0,0,0,.1);
}

/**************************************************************** TOP INFO TRACK *****************************************/

.track-top-info {    
    height: 50px;    
    display: flex;
    margin-bottom: 10px;
}

/************ play button start **************/

.main-play-button {
    font-size: 40px;
    color: #fe5621;
    margin-right: 10px;
    cursor: pointer;
}


/************ play button end **************/

.name-container {
    margin-top: 5px;
}

.name-artist .name-artist-a {
    color: #999;
    font-size: 12px;
    line-height: 16px;
    font-weight: 100;
}

.name-artist .name-artist-a:hover {
    color: #333;
}

.name-track .name-track-a {
    font-size: 15px;
    line-height: 1.2;
    font-weight: 100;
    color: #333;
}

.name-track .name-track-a:hover {
    color: #000;
}

.date-tag-container {
    margin-top: 8px;
    right: 0;
    position: absolute;
}

.date-tag-container .date-track {
    color: #ccc;
    font-size: 12px;
    font-weight: 100;
    line-height: 16px;
    text-align: right;
    margin-bottom: 5px;
}

.date-tag-container .tag-track {
    padding: 0 6px;
    line-height: 16px;
    font-size: 12px;    
    background: #999;
    border: 1px solid #999;    
    color: #fff;
    font-weight: 100;
    cursor: pointer;
    border-radius: 20px;
    position: absolute;
    right: 0;
}

.date-tag-container .tag-track:hover {
    background: #666;
    border: 1px solid #666;
    outline: 0;
}

/****************************************************** WAVE FORM ***************************************************/

.waveform ::part(progress) {
    height: 50%;
}

.waveform {
    cursor: pointer;
    position: relative; 
    width: 650px;
    height: 60px;   
}

.hover {
    position: absolute;
    left: 0;
    top: 0;
    z-index: 10;
    pointer-events: none;
    height: 50%;
    width: 0;
    mix-blend-mode: overlay;
    background: rgba(255, 255, 255, 0.5);
    opacity: 0;
    transition: opacity 0.2s ease;
}

.waveform:hover .hover {
    opacity: 1;
}

.time,
.duration {
    position: absolute;
    z-index: 11;
    top: 35%;
    margin-top: -1px;
    transform: translateY(-50%);
    font-size: 11px;
    background: rgba(0, 0, 0, 0.75);
    padding: 2px;
    color: #ddd;
}

.time {
    left: 0;
}

.duration {
    right: 0;
}

/******************************************************* BOTTOM INFO TRACK **********************************************/

.track-bottom-container {
    margin-top: 18px;
    display: inline-flex;
} 

.track-bottom-container .default-bt {
    display: inline-block;
    position: relative;
    margin-right: 5px;
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
    font-size: 11px;
    padding: 2px 9px 2px 8px;
    height: 22px;
    line-height: 16px;
}

.track-bottom-container .like-click {
    /* border: 1px solid #fe5621;  */
    color: #fe5621
}

.track-bottom-container .like-click:hover {
    border: 1px solid #fe5621; 
}

.track-bottom-container .fa-heart {
    margin-right: 3px;
}

.track-bottom-container .fa-heart, .track-bottom-container .like-button-text {
    pointer-events: none; /* off event target */
}

.track-bottom-container .buy-button {
    display: inline;
}

.track-bottom-container .buy-button .buy-button-a {    
    font-size: 11px;
    padding: 2px 9px 2px 8px;
    height: 22px;
    line-height: 16px;
    font-weight: 100;
    color: #333;
}

.track-bottom-container .buy-button .buy-button-a:hover {
    color: #000;
}

.play-like-repost-bottom {
    display: inline-flex;
    position: absolute;
    right: 0;
}


.play-like-repost-bottom .play-counter {
    font-size: 11px;
    padding: 2px 9px 2px 8px;
    height: 22px;
    line-height: 16px;
    font-weight: 100;
    color: #999999;
    margin-top: 2px;
}

.play-like-repost-bottom .repost-counter .repost-counter-a, 
.play-like-repost-bottom .comment-counter .comment-counter-a {
    font-size: 11px;
    padding: 2px 9px 2px 8px;
    height: 22px;
    line-height: 16px;
    font-weight: 100;
    color: #999999;
}

.play-like-repost-bottom .repost-counter .repost-counter-a:hover, 
.play-like-repost-bottom .comment-counter .comment-counter-a:hover {
    color: #333;
}

</style>