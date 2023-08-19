//*************************************************************************************************/
//**************************** INIT AND SETTINGS WAVE FORM ****************************************/
//*************************************************************************************************/

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



function getWaveForm(trackId, trackFile) {   

  // Create the waveform
  const wavesurfer = WaveSurfer.create({
    container: '#waveform' + trackId,
    waveColor: gradient,
    progressColor: progressGradient,
    barWidth: 2,
    height: 60,  
    url: trackFile,
  })

  // Hover effect
  const hover = document.querySelector('#hover' + trackId)
  const waveform = document.querySelector('#waveform' + trackId)
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
  const timeEl = document.querySelector('#time' + trackId)
  const durationEl = document.querySelector('#duration' + trackId)
  wavesurfer.on('decode', (duration) => (durationEl.textContent = formatTime(duration)))
  wavesurfer.on('timeupdate', (currentTime) => (timeEl.textContent = formatTime(currentTime)))

  // footer player
  const timeEl_player = document.querySelector('#time-line')
  const durationEl_player = document.querySelector('#duration-line')
  wavesurfer.on('decode', (duration) => (durationEl_player.textContent = formatTime(duration)))
  wavesurfer.on('timeupdate', (currentTime) => (timeEl_player.textContent = formatTime(currentTime)))


  //*****************************************************************************************************/
  //********************************* CATCH NAVIGATION BUTTONS *******************************************
  //******************************************************************************************************/


  const playMainButton = document.querySelector("#main-play-button" + trackId)
  // console.log(playMainButton)

  const playFooterButton = document.querySelector(".footer-play-button")
  const playFooterLine = document.querySelector(".footer-play-line-slider")
  const volumeFooterSlider = document.querySelector(".footer-volume-slider")
  const muteFooterButton = document.querySelector(".footer-speaker-button")

  // default settings
  let TrackDuration = 0 // init track duration
  let checkProgressValue = 0 // init progress
  let checkVolume = 0.2 // init volume
  wavesurfer.setVolume(checkVolume)

  wavesurfer.on('timeupdate', () => {
    TrackDuration = wavesurfer.getDuration() 
    playFooterLine.max = TrackDuration 
    checkProgressValue = wavesurfer.getCurrentTime()
    // playFooterLine.value = checkProgressValue 
    getProgress(checkProgressValue)
  }) 

  // play/pause on click
  wavesurfer.on('interaction', () => { 
    playMainButton.classList.add("playing")
    playFooterButton.classList.add("playing")
    wavesurfer.setVolume(checkVolume);
    checkProgressValue = wavesurfer.getCurrentTime()
    getProgress(checkProgressValue)
    wavesurfer.play()
  })

  // play/pause on main button
  playMainButton.addEventListener("click", () => { 
    if (wavesurfer.isPlaying()) {
      playMainButton.classList.remove("playing")
      wavesurfer.setVolume(checkVolume)
      playFooterButton.classList.remove("playing")
    } else {
      playMainButton.classList.add("playing")
      playFooterButton.classList.add("playing")
      if (muteFooterButton.classList.contains("muted")) {
          wavesurfer.setVolume(0)
      }   
    }   
    checkProgressValue = wavesurfer.getCurrentTime()
    getProgress(checkProgressValue)
    wavesurfer.playPause()
  })


  // play/pause on footer button
  playFooterButton.addEventListener("click", () => { 
    if (wavesurfer.isPlaying()) {
      playMainButton.classList.remove("playing")
      wavesurfer.setVolume(checkVolume)
      playFooterButton.classList.remove("playing")
    } else {
      playMainButton.classList.add("playing")
      playFooterButton.classList.add("playing")
      if (muteFooterButton.classList.contains("muted")) {
          wavesurfer.setVolume(0)
      }   
    }   
    checkProgressValue = wavesurfer.getCurrentTime()
    getProgress(checkProgressValue)
    wavesurfer.playPause()
  })

  // get volume on mouse
  volumeFooterSlider.addEventListener("mouseup", () => {
    changeVolume(volumeFooterSlider.value)     
  })

  // set volume
  const changeVolume = (volume) => {
    if (volume == 0) {
      muteFooterButton.classList.add("muted")
    } else {
      muteFooterButton.classList.remove("muted")
    }
    checkVolume = volume;
    wavesurfer.setVolume(volume)  
  }

  // mute button
  muteFooterButton.addEventListener("click", () => {
    if (muteFooterButton.classList.contains("muted")) {
      muteFooterButton.classList.remove("muted")
      wavesurfer.setVolume(checkVolume)    
    } else {    
      wavesurfer.setVolume(0)    
      muteFooterButton.classList.add("muted")    
    }  
  })

  //*********************************************************

  // volume slider animation
  // init condition
  let tempSliderValue = checkVolume
  volumeFooterSlider.style.background = `linear-gradient(to right, #f50 ${tempSliderValue*100}%, #ccc ${tempSliderValue*100}%)`

  // set volume
  volumeFooterSlider.addEventListener("input", (event) => {
    tempSliderValue = event.target.value  
    volumeFooterSlider.style.background = `linear-gradient(to right, #f50 ${tempSliderValue*100}%, #ccc ${tempSliderValue*100}%)`
  })

  //*************************************************************

  // progress line animation
  function getProgress(progress){
    playFooterLine.value = progress   
    playFooterLine.style.background = `linear-gradient(to right, #f50 ${progress*(100/TrackDuration)}%, #ccc ${progress*(100/TrackDuration)}%)`
  }

  // set progress
  playFooterLine.addEventListener("input", (event) => {
    progress = event.target.value
    playFooterLine.style.background = `linear-gradient(to right, #f50 ${progress*(100/TrackDuration)}%, #ccc ${progress*(100/TrackDuration)}%)`
  })

  // get time on mouse
  playFooterLine.addEventListener("input", () => {
    changeProgress(playFooterLine.value) 
    wavesurfer.play()  
    playMainButton.classList.add("playing")
    playFooterButton.classList.add("playing")
  })

  const changeProgress = (Time) => {  
    wavesurfer.setTime(Time) 
  }

}