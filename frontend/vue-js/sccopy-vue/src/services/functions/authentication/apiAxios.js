import axios from 'axios'

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
    console.log(error)
}) // error from frontend

//--------------------------- end request ---------------------------


//--------------------------- start response ------------------------

apiAxios.interceptors.response.use(config => {

    if (localStorage.getItem('accessToken')) {
        config.headers.authorization = `JWT ${localStorage.getItem('accessToken')}`        
    }  
    return config

}, error => {
    if (error.response.data.message === 'Token has expired') {
        return axios.post(import.meta.env.VITE_API_REFRESH_TOKEN, {
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