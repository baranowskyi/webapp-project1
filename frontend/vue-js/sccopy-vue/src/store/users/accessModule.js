export default {     
    namespaced: true, 
    state: {
        accessToken: '',
        refreshToken: '',
    },
    mutations: {
        initializationStore(state) {
            if ( localStorage.getItem("accessToken") ) {
                state.accessToken = localStorage.getItem("accessToken")
            }
            else {
                state.accessToken = ''                
            }
            if ( localStorage.getItem("refreshToken") ) {
                state.refreshToken = localStorage.getItem("refreshToken")
            }
            else {
                state.refreshToken = ''                
            }
        },
        setAccessToken(state, accessToken) {
            state.accessToken = accessToken
        },
        setRefreshToken(state, refreshToken) {
            state.refreshToken = refreshToken
        }
        
    },
    getters: {
        getAccessToken(state) {
            return state.accessToken
        },
        getRefreshToken(state) {
            return state.refreshToken
        }
    }    
}

