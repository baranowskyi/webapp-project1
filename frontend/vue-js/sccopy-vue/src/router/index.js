import { createRouter, createWebHistory } from 'vue-router'
import titlePage from '@/services/constants/titlePage.js'

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
            path: '/:artist',
            name: 'artist-all',      
            component: () => import('@/views/ArtistAll.vue'),
            meta: { 
                title: titlePage.artistAll,
                layout: "MainLayout",
            }, 
        },  
        {
            path: '/:artist/popular-tracks',
            name: 'artist-popular-tracks',
            component: () => import('@/views/ArtistPopularTracks.vue'),
            meta: { 
                title: titlePage.artistPopularTracks,
                layout: "MainLayout", 
            },      
        },
        {
            path: '/:artist/tracks',
            name: 'artist-tracks',
            component: () => import('@/views/ArtistTracks.vue'),
            meta: { 
                title: titlePage.artistTracks, 
                layout: "MainLayout",
            },      
        },
        {
            path: '/:artist/albums',
            name: 'artist-albums',
            component: () => import('@/views/ArtistAlbums.vue'),
            meta: { 
                title: titlePage.artistAlbums, 
                layout: "MainLayout",
            },      
        },
        {
            path: '/:artist/sets',
            name: 'artist-sets',
            component: () => import('@/views/ArtistPlaylists.vue'),
            meta: { 
                title: titlePage.artistPlaylists,
                layout: "MainLayout",
            },      
        },
        {
            path: '/:artist/reposts',
            name: 'artist-reposts',
            component: () => import('@/views/ArtistReposts.vue'),
            meta: { 
                title: titlePage.artistReposts,
                layout: "MainLayout", 
            },      
        },     
                  
          

    ]
})

export default router
