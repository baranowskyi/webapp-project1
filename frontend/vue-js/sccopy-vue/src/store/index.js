import { createStore } from 'vuex'
import accessModule from '@/store/users/accessModule.js'
import headerNavbarActions from '@/store/header-navbar/headerNavbarActions.js'
import currentArtist from '@/store/artist/currentArtist.js'

export default createStore({
    modules: {
        accessModule, 
        headerNavbarActions,   
        currentArtist,    
    },
    
})

