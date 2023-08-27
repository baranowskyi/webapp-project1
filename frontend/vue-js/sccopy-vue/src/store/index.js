import { createStore } from 'vuex'
import accessModule from '@/store/users/accessModule.js'
import headerNavbarActions from '@/store/header-navbar/headerNavbarActions.js'

export default createStore({
    modules: {
        accessModule, 
        headerNavbarActions,       
    },
    
})

