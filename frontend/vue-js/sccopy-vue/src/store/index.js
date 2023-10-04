import { createStore, createLogger } from 'vuex'
import accessModule from '@/store/users/accessModule.js'
import modalForm from '@/store/modalForm.js'
import currentArtist from '@/store/artist/currentArtist.js'
import currentSong from '@/store/player/currentSong.js'
import tracksArtist from '@/store/artist/tracksArtist.js'

const store = createStore({
    modules: {
        accessModule, 
        modalForm,   
        currentArtist, 
        currentSong,  
        tracksArtist, 
    },
    plugins: [createLogger()], // console logger
    devtools: true, // use browser devtools 
    
})

export default store
