import { createStore, createLogger } from 'vuex'
import accessModule from '@/store/users/accessModule.js'
import modalForm from '@/store/modalForm.js'
import currentArtist from '@/store/artist/currentArtist.js'

const store = createStore({
    modules: {
        accessModule, 
        modalForm,   
        currentArtist,    
    },
    plugins: [createLogger()], // console logger
    devtools: true, // use browser devtools 
    
})

export default store
