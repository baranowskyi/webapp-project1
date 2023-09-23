export default {     
    namespaced: true, 
    state: {
        isLoginModalForm: false,              
    },
    mutations: {        
        SET_LOGIN_MODAL_FORM(state, isLoginModalForm) {
            state.isLoginModalForm = isLoginModalForm
        },      
        
    },
    getters: {
        LOGIN_MODAL_FORM(state) {
            return state.isLoginModalForm
        },
         
    }    
}