import apiAxios from '@/services/functions/authentication/apiAxios.js'

export default {     
    namespaced: true,     
    state: {
        tracksArtist: [],
         
    },
    mutations: {
        SET_TRACKS_ARTIST(state) {            
            if ( localStorage.getItem("tracksArtist") ) {                
                const parseData = JSON.parse(localStorage.getItem("tracksArtist"))
                state.tracksArtist = parseData                                
            } 
            else {
                state.tracksArtist = []                
            }   
        } 
    },
    actions: {
        async GET_TRACKS_ARTIST({commit}, artist) {

            try {
                
                // VITE_API_TRACKS_ARTIST = api/[artist]/show-tracks/
                const URL = import.meta.env.VITE_API_TRACKS_ARTIST.replace(/\[artist\]/i, artist) 

                const response = await apiAxios.get(URL)

                if (response.status == 200) { 

                    localStorage.setItem("tracksArtist", JSON.stringify(response.data)) 

                    commit('SET_TRACKS_ARTIST')
                } 
                
            }
            catch (error) {                
                console.error(error)                    
            }
        }
    },
    getters: {
        ALL_TRACKS_ARTIST(state) {
            return state.tracksArtist
        },
        

    },
    
}