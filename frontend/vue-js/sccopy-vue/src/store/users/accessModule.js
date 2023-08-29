export default {     
    namespaced: true, 
    state: {
        accessToken: '',
        refreshToken: '',
        isAuthenticated: false,
        userID: '',
        userName: ''

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
        },
        setIsAuthenticated(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated
        },
        setUserID(state, userID) {
            state.userID = userID
        },
        setUserName(state, userName) {
            state.userName = userName
        },
        
    },
    getters: {
        getAccessToken(state) {
            return state.accessToken
        },
        getRefreshToken(state) {
            return state.refreshToken
        },
        getIsAuthenticated(state) {
            return state.isAuthenticated
        },
        getUserID(state) {
            return state.userID
        },
        getUserName(state) {
            return state.userName
        }
    }    
}

