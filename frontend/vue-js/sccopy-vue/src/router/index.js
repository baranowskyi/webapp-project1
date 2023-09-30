import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'
import { 
    ARTIST_ALL, 
    ARTIST_POPULAR_TRACKS, 
    ARTIST_TRACKS, 
    ARTIST_ALBUMS, 
    ARTIST_PLAYLISTS, 
    ARTIST_REPORTS
} from '@/services/constants/titlePage.js'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [ 
        {
            path: '/:pathMatch(.*)*',
            name: 'page-not-found',
            component: () => import('@/views/PageNotFound404.vue'),                        
            meta: { 
                title: "page-not-found",
                layout: "EmptyLayout"
            },
        }, 
        
        {
            path: '/artist-not-found',
            name: 'artist-not-found',
            component: () => import('@/views/PageNotFoundArtist.vue'),
            meta: { 
                title: "Someting went wrong on SCCopy",
                layout: "EmptyLayout"
            },
        },
        {
            path: '/:artist',
            name: 'artist-all',      
            component: () => import('@/views/ArtistAll.vue'),
            meta: { 
                title: ARTIST_ALL,
                layout: "MainLayout",
            }, 
        },  
        {
            path: '/:artist/popular-tracks',
            name: 'artist-popular-tracks',
            component: () => import('@/views/ArtistPopularTracks.vue'),
            meta: { 
                title: ARTIST_POPULAR_TRACKS,
                layout: "MainLayout", 
            },      
        },
        {
            path: '/:artist/tracks',
            name: 'artist-tracks',
            component: () => import('@/views/ArtistTracks.vue'),
            meta: { 
                title: ARTIST_TRACKS, 
                layout: "MainLayout",
            },      
        },
        {
            path: '/:artist/albums',
            name: 'artist-albums',
            component: () => import('@/views/ArtistAlbums.vue'),
            meta: { 
                title: ARTIST_ALBUMS, 
                layout: "MainLayout",
            },      
        },
        {
            path: '/:artist/sets',
            name: 'artist-sets',
            component: () => import('@/views/ArtistPlaylists.vue'),
            meta: { 
                title: ARTIST_PLAYLISTS,
                layout: "MainLayout",
            },      
        },
        {
            path: '/:artist/reposts',
            name: 'artist-reposts',
            component: () => import('@/views/ArtistReposts.vue'),
            meta: { 
                title: ARTIST_REPORTS,
                layout: "MainLayout", 
            },      
        }, 
    ],
    

})

router.beforeEach((to, from, next) => {     
    const artist = store.getters["currentArtist/DISPLAY_NAME"]
    console.log("router.beforeEach >>> ", artist)
    document.title = to.meta.title.replace(/\[artist\]/i, artist)    
    next()
})

export default router
