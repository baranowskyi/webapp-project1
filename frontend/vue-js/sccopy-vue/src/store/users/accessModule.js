export default {     
    namespaced: true, 
    state: {
        accessToken: '',                
        isAuthenticated: false,
        userData: {
            userID: '',
            userName: '',
            userEmail: '',
        }
         
    },
    mutations: {
        SET_AUTHENTICATION_DATA(state) {
            if ( localStorage.getItem("accessToken") ) {
                state.accessToken = localStorage.getItem("accessToken")
            }
            else {
                state.accessToken = ''                
            }         
            
            if ( localStorage.getItem("isAuthenticated") ) {
                state.isAuthenticated = localStorage.getItem("isAuthenticated")
            }
            else {
                state.isAuthenticated = false                
            } 
            if ( localStorage.getItem("userData") ) {
                
                const parseUserData = JSON.parse(localStorage.getItem("userData"))

                state.userData.userID = parseUserData.userID
                state.userData.userName = parseUserData.userName
                state.userData.userEmail = parseUserData.userEmail                
            } 
            else {
                state.userData.userID = ''
                state.userData.userName = ''
                state.userData.userEmail = ''
            }   
        },
        setAccessToken(state, accessToken) {
            state.accessToken = accessToken
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
        getIsAuthenticated(state) {
            return state.isAuthenticated
        },
        getUserID(state) {
            return state.userID
        },
        getUserName(state) {
            return state.userName
        },        
    }    
}

