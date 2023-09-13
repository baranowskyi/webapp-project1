import { createStore, createLogger } from 'vuex'
import accessModule from '@/store/users/accessModule.js'
import headerNavbarActions from '@/store/header-navbar/headerNavbarActions.js'
import currentArtist from '@/store/artist/currentArtist.js'

const store = createStore({
    modules: {
        accessModule, 
        headerNavbarActions,   
        currentArtist,    
    },
    plugins: [createLogger()], // console logger
    devtools: true, // use browser devtools 
    
})

export default store
