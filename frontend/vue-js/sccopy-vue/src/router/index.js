import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [  
    {
      path: '/',
      name: 'home',
      component: () => import('../views/ArtistAll.vue'),
    },  
    {
      path: '/:slug_artist',
      name: 'artist-all',
      // lazy load
      component: () => import('../views/ArtistAll.vue'),
      meta: {title: "All"}
    },
    {
      path: '/:slug_artist/popular-tracks',
      name: 'artist-popular-tracks',
      component: () => import('../views/ArtistPopularTracks.vue'),
      meta: {title: "Popular tracks"}
    },
    {
      path: '/:slug_artist/tracks',
      name: 'artist-tracks',
      component: () => import('../views/ArtistTracks.vue'),
      meta: {title: "Tracks"}
    },
    {
      path: '/:slug_artist/albums',
      name: 'artist-albums',
      component: () => import('../views/ArtistAlbums.vue'),
      meta: {title: "Albums"}
    },
    {
      path: '/:slug_artist/sets',
      name: 'artist-playlists',
      component: () => import('../views/ArtistPlaylists.vue'),
      meta: {title: "Playlists"}
    },
    {
      path: '/:slug_artist/reposts',
      name: 'artist-reposts',
      component: () => import('../views/ArtistReposts.vue'),
      meta: {title: "Reposts"}
    },
  ]
})

export default router
