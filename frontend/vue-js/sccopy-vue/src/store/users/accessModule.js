export default {     
    namespaced: true, 
    state: {
        accessToken: '',                
        isAuthenticated: false,
        userData: {
            userID: '',
            userName: '',
            // userEmail: '',
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
                // state.userData.userEmail = parseUserData.userEmail                
            } 
            else {
                state.userData.userID = ''
                state.userData.userName = ''
                // state.userData.userEmail = ''
            }   
        },
        SET_ACCESS_TOKEN(state, accessToken) {
            state.accessToken = accessToken
        },        
        SET_IS_AUTHENTICATED(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated
        },
        // SET_USER_ID(state, userID) {
        //     state.userID = userID
        // },
        // SET_USER_NAME(state, userName) {
        //     state.userName = userName
        // }, 
    },
    getters: {
        ACCESS_TOKEN(state) {
            return state.accessToken
        },        
        IS_AUTHENTICATED(state) {
            return state.isAuthenticated
        },
        USER_ID(state) {
            return state.userData.userID
        },
        USER_NAME(state) {
            return state.userData.userName
        },        
    }    
}

