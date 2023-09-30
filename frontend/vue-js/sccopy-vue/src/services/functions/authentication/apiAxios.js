import axios from 'axios'
import { ARTIST_DOES_NOT_EXIST } from '@/services/constants/errorMessages.js'
import router from '@/router'

const apiAxios = axios.create()

apiAxios.defaults.baseURL = import.meta.env.VITE_MAIN_URL
apiAxios.defaults.headers.common['Content-Type'] = 'application/json'
apiAxios.defaults.withCredentials = true
apiAxios.defaults.xsrfCookieName = 'csrftoken'
apiAxios.defaults.xsrfHeaderName = 'X-CSRFToken'

//-------------------------- start request -------------------------

apiAxios.interceptors.request.use(config => {

    if (localStorage.getItem('accessToken')) {
        config.headers.authorization = `JWT ${localStorage.getItem('accessToken')}`        
    }    
    return config

}, error => {
    console.log("axios interceptors request >>> ", error)
}) // error from frontend

//--------------------------- end request ---------------------------


//--------------------------- start response ------------------------

apiAxios.interceptors.response.use(config => {

    if (localStorage.getItem('accessToken')) {
        config.headers.authorization = `JWT ${localStorage.getItem('accessToken')}`        
    }  
    return config

}, error => {
    console.log("axios interceptors response >>> ", error.response)

    if (error.response.data.detail === ARTIST_DOES_NOT_EXIST) {
        router.push('artist-not-found')
        console.log("push page not found")
    }
    if (error.response.data.message === 'Token has expired') {
        return apiAxios.post(import.meta.env.VITE_API_REFRESH_TOKEN, {
            headers: {
                'authorization': `JWT ${localStorage.getItem('accessToken')}`
            }
        }).then( res => {
            localStorage.setItem('accessToken', res.data.accessToken)
            error.config.headers.authorization = `JWT ${res.data.accessToken}`
            return apiAxios.request(error.config)
        })
    }
}) // error from backend

//--------------------------- end response --------------------------

export default apiAxios