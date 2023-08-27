import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'

//------------------------ FontAwesome ----------------------

// import the fontawesome core 
import { library } from '@fortawesome/fontawesome-svg-core'
// import font awesome icon component
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// import specific icons
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
//import { far } from '@fortawesome/free-regular-svg-icons'

//-----------------------------------------------------------

// add icons FontAwesome to the library
library.add(fas, fab)

// default axios main URL (http://127.0.0.1:8000) from .env
axios.defaults.baseURL = import.meta.env.VITE_MAIN_URL

createApp(App)
.use(router, store, axios)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')
