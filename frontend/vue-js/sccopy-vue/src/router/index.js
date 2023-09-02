import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ 
    {
      path: '/:pathMatch(.*)*',
      name: 'page-not-found',
      component: () => import('@/views/PageNotFound404.vue'),
      meta: { title: "page-not-found" },
    },
    {
      path: '/:artist',
      name: 'artist-all',      
      component: () => import('@/views/ArtistAll.vue'),
      meta: { title: "All" },
      props: true,
    },
    {
      path: '/:artist/popular-tracks',
      name: 'artist-popular-tracks',
      component: () => import('@/views/ArtistPopularTracks.vue'),
      meta: { title: "Popular tracks" },
      props: true,
    },
    {
      path: '/:artist/tracks',
      name: 'artist-tracks',
      component: () => import('@/views/ArtistTracks.vue'),
      meta: { title: "Tracks" },
      props: true,
    },
    {
      path: '/:artist/albums',
      name: 'artist-albums',
      component: () => import('@/views/ArtistAlbums.vue'),
      meta: { title: "Albums" },
      props: true,
    },
    {
      path: '/:artist/sets',
      name: 'artist-playlists',
      component: () => import('@/views/ArtistPlaylists.vue'),
      meta: { title: "Playlists" },
      props: true,
    },
    {
      path: '/:artist/reposts',
      name: 'artist-reposts',
      component: () => import('@/views/ArtistReposts.vue'),
      meta: { title: "Reposts" },
      props: true,
    },
    
  ]
})

export default router
