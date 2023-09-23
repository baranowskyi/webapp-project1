<template>
    <div class="footer-player">
        <div class="footer-buttons">
    
            <!-- navigation button -->
            <span class="footer-back-button button-st">
                <font-awesome-icon icon="fa-solid fa-backward-step"/>      
            </span> 
            <span class="footer-play-button button-st">
                <font-awesome-icon icon="fas fa-play"/>
                <font-awesome-icon icon="fas fa-pause"/>
            </span>  
            <span class="footer-next-button button-st">
                <font-awesome-icon icon="fa-solid fa-forward-step"/>      
            </span>
            <span class="footer-repeat-button button-st">
                <font-awesome-icon icon="fa-solid fa-repeat"/>      
            </span>
        
            <!-- progress line -->
            <div class="footer-container-line-and-time">
                <div class="footer-play-line-start button-st">
                    <div style="color: #fe5621" id="time-line">0:00</div>      
                </div>
                <div class="footer-container-play-line">
                    <input class="footer-play-line-slider slider" type="range" min="0" max="" step="any" value="0" />
                </div>
                <div class="footer-play-line-end button-st">      
                    <div id="duration-line">0:00</div>
                </div>
            </div> 
        
            <!-- mute\unmute and volume -->
            <div class="footer-speaker-container">
            <span class="footer-speaker-button">
                <font-awesome-icon icon="fas fa-volume-up"/>
                <font-awesome-icon icon="fas fa-volume-mute"/>
            </span> 
            <div class="footer-container-volume">
                <input class="footer-volume-slider slider" type="range" min="0" max="1" step="any" value="0.2" />
            </div> 
            </div>
    
            <!-- mini info -->
            <div class="mini-player">
            <div class="mini-cover-bottom">
                <img class="mini-cover-img" src="">
            </div>
            <div class="mini-info-bottom">
                <div class="mini-name-artist"><a class="mini-name-artist-a" href="#">Artist</a></div>
                <div class="mini-name-track"><a class="mini-name-track-a" href="#">A Living Room </a></div>
            </div>
            <div class="mini-like-follow-list">
                <div class="mini-like"><a class="mini-like-a" href="#"><font-awesome-icon icon="fa-solid fa-heart"/></a></div>
                <div class="mini-follow"><a class="mini-follow-a" href="#"><font-awesome-icon icon="fa-solid fa-user-check"/></a></div>
                <div class="mini-list"><a class="mini-list-a" href="#"><font-awesome-icon icon="fa-solid fa-list-check"/></a></div>
            </div>
            </div>
        
        </div>
    </div>  
</template>

<script>

</script>

<style scoped>

/******************************************** SLIDER MAIN SLYLE *************************************************/

.slider { 
    -webkit-appearance: none;
    appearance: none;     
    cursor: pointer;
    outline: none;
    border-radius: 15px;
    height: 2px;
    background: #ccc;
  }
  
.slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none; 
    height: 10px;
    width: 10px;
    background-color: #f50;
    border-radius: 50%;
    border: none;
    transition: .2s ease-in-out;
  }
  
.slider::-moz-range-thumb {
    height: 15px;
    width: 15px;
    background-color: #f50;
    border-radius: 50%;
    border: none;
    transition: .2s ease-in-out;
}

/**************************************************************************************************/
/************************************************* FOOTER PLAYER *********************************/
/**************************************************************************************************/ 

.footer-player {
    height: 48px;
    background-color: #f2f2f2;
    border: 1px solid #cccccc;
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 999;
}  

/*********************************************************************** NAV BUTTON ******************************************/

.footer-buttons {       
    display: flex;    
    width: 1240px;
    margin: 0 auto;
}

.button-st {
    width: 7px;
    margin: 15px;
    cursor: pointer;
    font-size: 15px;
}

.footer-player .footer-buttons .footer-play-button .fa-pause {
    display: none;
}
  
.footer-player .footer-buttons .footer-play-button.playing .fa-pause {
    display: inline-block;
}

.footer-player .footer-buttons .footer-play-button.footer-play-button.playing .fa-play {
    display: none;
}

/***************************************************************** PROGRESS LINE SLIDER **************************************/

.footer-container-line-and-time {
    margin-left: 25px;
    margin-right: 25px;
    display: flex;
} 

.footer-container-play-line {
    margin: 10px;
    margin-left: 20px;
}

.footer-play-line-start {
    position: relative;
}

.footer-play-line-end {
    position: relative;
}

#time-line, #duration-line {
    font-size: 12px;
}

.footer-play-line-slider {  
    width: 500px;
}

.footer-container-play-line .slider::-webkit-slider-thumb {
    display: none;
}

.footer-container-play-line:hover .slider::-webkit-slider-thumb {
    display: block;
}

/*************************************************************** VOLUME SLIDER *************************************/  

.footer-speaker-container {
    position: relative;
    display: flex;
    width: 90px;
}
 
.footer-container-volume {
    background-color: #f2f2f2;
    height: 125px;
    width: 30px;
    border: 1px solid #cccccc;
    position: relative;
    bottom: 115px;
    right: 28px;
    display: none; 
}

.footer-volume-slider {  
    width: 100px;
    position: relative;
    top: 50px;
    left: -37px;    
    transform: rotate(-90deg);
}

.footer-container-volume:hover {
    display: inline-block       
}

/**************** mute\unmute start ***********/

.footer-speaker-button {
    height: 48px;
    width: 35px;
    font-size: 15px;
    padding: 13px;
    cursor: pointer;
}

.footer-speaker-container .footer-speaker-button .fa-volume-mute {
    display: none;
}

.footer-speaker-container .footer-speaker-button.muted .fa-volume-mute {
    display: inline-block;
}

.footer-speaker-container .footer-speaker-button.muted .fa-volume-up {
    display: none;
}

.footer-speaker-button:hover ~ .footer-container-volume {
    display: inline-block    
}

/**************** mute\unmute end ***********/

/*************************************************************** MINI PLAYER INFO ***********************************************/

.mini-player {
    display: flex;    
    height: 40px;
    width: 500px;
}

.mini-cover-bottom {
    width: 30px;
    height: 30px;
    margin: 10px;
    margin-left: 0px;
}

.mini-cover-bottom .mini-cover-img {
    width: 100%;
    height: 100%;
    cursor: pointer;
}

.mini-info-bottom {
    margin-top: 7px;
    width: 240px;
}

.mini-info-bottom .mini-name-artist,
.mini-info-bottom .mini-name-track {
    margin: 0 auto;
    height: 15px;
}

.mini-info-bottom .mini-name-artist .mini-name-artist-a,
.mini-info-bottom .mini-name-track .mini-name-track-a {
    font-size: 12px;
    color: #666;
}

.mini-info-bottom .mini-name-artist .mini-name-artist-a:hover,
.mini-info-bottom .mini-name-track .mini-name-track-a:hover {
    color: #000;
}

.mini-like-follow-list {
    display: flex;    
}

.mini-like-follow-list .mini-like,
.mini-like-follow-list .mini-follow,
.mini-like-follow-list .mini-list {
    margin-left: 13px;
    margin-top: 13px;
    font-size: 12px;
}

.mini-like-follow-list .mini-like .mini-like-a,
.mini-like-follow-list .mini-follow .mini-follow-a,
.mini-like-follow-list .mini-list .mini-list-a {
    color: #222222;    
}

</style>