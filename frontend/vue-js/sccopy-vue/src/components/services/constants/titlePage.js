import store from '@/store'

const titlePage = {
    artistAll: `Stream ${store.getters["currentArtist/GET_DISPLAY_NAME"]} music | Listen to songs, albums, playlists for free on SCCopy`,
    artistPopularTracks: `Stream ${store.getters["currentArtist/GET_DISPLAY_NAME"]} | Listen to top hits and popular tracks online for free on SCCopy`,
    artistTracks: `Stream ${store.getters["currentArtist/GET_DISPLAY_NAME"]} | Listen to tracks online for free on SCCopy`,
    artistAlbums: `Stream ${store.getters["currentArtist/GET_DISPLAY_NAME"]} | Listen to music albums online for free on SCCopy`,
    artistPlaylists: `Stream ${store.getters["currentArtist/GET_DISPLAY_NAME"]} | Listen to music playlists online for free on SCCopy`,
    artistReposts: `Listen to ${store.getters["currentArtist/GET_DISPLAY_NAME"]}'s favorite music online for free on SCCopy`
}

export default titlePage