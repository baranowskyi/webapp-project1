export default {     
    namespaced: true, 
    state: {
        currentArtistData: {
            artistID: '',
            username: '',
            proUser: '',
            displayName: '',
            slugArtist: '',
            profileUrl: '',
            avatarImage: '',
            avatarImageSmall: '',
            headerImage: '',
            verification: '',
            firstName: '',
            lastName: '',
            city: '',
            country: '',
            bio: '',
        }
         
    },
    mutations: {
        SET_CURRENT_ARTIST_DATA(state) {
            
            if ( localStorage.getItem("currentArtistData") ) {
                
                const parseCurrentArtistData = JSON.parse(localStorage.getItem("currentArtistData"))

                state.currentArtistData.artistID = parseCurrentArtistData.artistID
                state.currentArtistData.username = parseCurrentArtistData.username
                state.currentArtistData.proUser = parseCurrentArtistData.proUser
                state.currentArtistData.displayName = parseCurrentArtistData.displayName
                state.currentArtistData.slugArtist = parseCurrentArtistData.slugArtist
                state.currentArtistData.profileUrl = parseCurrentArtistData.profileUrl
                state.currentArtistData.avatarImage = parseCurrentArtistData.avatarImage
                state.currentArtistData.avatarImageSmall = parseCurrentArtistData.avatarImageSmall
                state.currentArtistData.headerImage = parseCurrentArtistData.headerImage
                state.currentArtistData.verification = parseCurrentArtistData.verification
                state.currentArtistData.firstName = parseCurrentArtistData.firstName
                state.currentArtistData.lastName = parseCurrentArtistData.lastName
                state.currentArtistData.city = parseCurrentArtistData.city
                state.currentArtistData.country = parseCurrentArtistData.country
                state.currentArtistData.bio = parseCurrentArtistData.bio
                                
            } 
            else {
                state.currentArtistData.artistID = ''
                state.currentArtistData.username = ''
                state.currentArtistData.proUser = ''
                state.currentArtistData.displayName = ''
                state.currentArtistData.slugArtist = ''
                state.currentArtistData.profileUrl = ''
                state.currentArtistData.avatarImage = ''
                state.currentArtistData.avatarImageSmall = ''
                state.currentArtistData.headerImage = ''
                state.currentArtistData.verification = ''
                state.currentArtistData.firstName = ''
                state.currentArtistData.lastName = ''
                state.currentArtistData.city = ''
                state.currentArtistData.country = ''
                state.currentArtistData.bio = ''
            }   
        },
        SET_AVATAR_IMAGE_SMALL(state, avatarImageSmall) {
            state.currentArtistData.avatarImageSmall = avatarImageSmall
        },        
        
    },
    getters: {
        GET_AVATAR_IMAGE_SMALL(state) {
            return state.currentArtistData.avatarImageSmall
        },        
       
    }    
}