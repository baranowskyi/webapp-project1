
export const userIsAuthenticatedMixin = {

    data() {
        return {             
            userIsAuthenticated: false                    
        }
    },

    computed: {
        getUserStatus() {
            this.userIsAuthenticated = this.$store.getters["accessModule/IS_AUTHENTICATED"]
        }            
    },

    watch: {
        getUserStatus() {
            this.userIsAuthenticated         
        }
    }

}