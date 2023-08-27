export default {     
    namespaced: true, 
    state: {
        isLoginButton: false,        
    },
    mutations: {        
        setLoginButton(state, isLoginButton) {
            state.isLoginButton = isLoginButton
        },       
        
    },
    getters: {
        getLoginButton(state) {
            return state.isLoginButton
        },        
    }    
}