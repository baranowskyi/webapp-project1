
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


export const artistDisplayNameMixin = {

    data() {
        return {             
            artistDisplayName: null                    
        }
    },

    computed: {
        getArtistDisplayName() {
            this.artistDisplayName = this.$store.getters["currentArtist/DISPLAY_NAME"]
        }            
    },

    watch: {
        getArtistDisplayName() {
            this.artistDisplayName         
        }
    }

}