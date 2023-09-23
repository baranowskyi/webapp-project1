
const artistDisplayName = this.$store.getters["currentArtist/DISPLAY_NAME"]

const titlePage = {
    artistAll: `Stream ${artistDisplayName} music | Listen to songs, albums, playlists for free on SCCopy`,
    artistPopularTracks: `Stream ${artistDisplayName} | Listen to top hits and popular tracks online for free on SCCopy`,
    artistTracks: `Stream ${artistDisplayName} | Listen to tracks online for free on SCCopy`,
    artistAlbums: `Stream ${artistDisplayName} | Listen to music albums online for free on SCCopy`,
    artistPlaylists: `Stream ${artistDisplayName} | Listen to music playlists online for free on SCCopy`,
    artistReposts: `Listen to ${artistDisplayName}'s favorite music online for free on SCCopy`
}

export default titlePage