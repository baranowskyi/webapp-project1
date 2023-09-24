import apiAxios from '@/services/functions/authentication/apiAxios.js'

export default {     
    namespaced: true,     
    state: {
        currentArtistData: [],
         
    },
    mutations: {
        SET_CURRENT_ARTIST_DATA(state) {            
            if ( localStorage.getItem("currentArtistData") ) {                
                const parseData = JSON.parse(localStorage.getItem("currentArtistData"))
                state.currentArtistData = parseData                                
            } 
            else {
                state.currentArtistData = []                
            }   
        } 
    },
    actions: {
        async GET_CURRENT_ARTIST_DATA({commit}) {

            localStorage.removeItem("currentArtistData")

            try {
                let response = await apiAxios.get(import.meta.env.VITE_API_CURRENT_ARTIST)
                response = response.data[0]                

                const currentArtistData = {
                    artistID: response.id,
                    username: response.username.username,
                    proUser: response.username.pro_user,
                    displayName: response.display_name,
                    slugArtist: response.slug_artist,
                    profileUrl: response.profile_url,
                    avatarImage: response.avatar_image,
                    avatarImageSmall: response.avatar_image_small,
                    headerImage: response.header_image,
                    verification: response.verification,
                    firstName: response.first_name,
                    lastName: response.last_name,
                    city: response.city,
                    country: response.country,
                    bio: response.bio,
                }

                localStorage.setItem("currentArtistData", JSON.stringify(currentArtistData)) 

                commit('SET_CURRENT_ARTIST_DATA')
                
            }
            catch (error) {                
                console.log(error.status)
            }
        }
    },
    getters: {
        ALL_ARTIST_DATA(state) {
            return state.currentArtistData
        },
        ARTIST_ID(state) {
            return state.currentArtistData.artistID
        },
        USERNAME(state) {
            return state.currentArtistData.username
        },
        PRO_USER(state) {
            return state.currentArtistData.proUser
        },
        DISPLAY_NAME(state) {
            return state.currentArtistData.displayName
        },
        SLUG_ARTIST(state) {
            return state.currentArtistData.slugArtist
        },
        // PROFILE_URL() {
        //     return state.currentArtistData.profileUrl
        // },
        AVATAR_IMAGE(state) {
            return state.currentArtistData.avatarImage
        },        
        AVATAR_IMAGE_SMALL(state) {
            return state.currentArtistData.avatarImageSmall
        },
        HEADER_IMAGE(state) {
            return state.currentArtistData.headerImage
        },
        VERIFICATION(state) {
            return state.currentArtistData.verification
        },
        FIRST_NAME(state) {
            return state.currentArtistData.firstName
        },
        LAST_NAME(state) {
            return state.currentArtistData.lastName
        },
        CITY(state) {
            return state.currentArtistData.city
        },
        COUNTRY(state) {
            return state.currentArtistData.country
        },
        BIO(state) {
            return state.currentArtistData.bio
        }

    },
    
}