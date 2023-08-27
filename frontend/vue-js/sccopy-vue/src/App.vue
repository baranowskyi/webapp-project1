<script>

import { RouterLink, RouterView } from 'vue-router'
import HeaderNavbar from '@/components/header-navbar/HeaderNavbar.vue'
import ModalLoginForm from '@/components/modal/ModalLoginForm.vue'
import axios from 'axios'
import store from './store'


export default {
    name: "App",    
    components: {
        HeaderNavbar,  
        ModalLoginForm,
    },    
    beforeCreate() {          
        store.commit("accessModule/initializationStore") 
        const accessToken = store.getters["accessModule/getAccessToken"] 
        console.log("accessToken from STORE =", accessToken)

        if ( accessToken ) {
            axios.defaults.headers.common["Authorization"] = "JWT " + accessToken
        }
        else {
            axios.defaults.headers.common["Authorization"] = ''
        }        
    },
    // mounted() {
    //     setInterval(() => {
    //         this.upadateToken()
    //     }, 10000)
    // },
    mounted() {
        this.upadateToken()
    },
    methods: {
        upadateToken() {
            const accessData = {
                refresh: store.getters["accessModule/getRefreshToken"]
            }
            
            axios
                .post("api/auth/jwt/refresh/", accessData, {headers: {"Content-type": "application/json"}}, {withCredentials: true})
                .then(response => {
                    const accessToken = response.data.access

                    console.log("new Token =", accessToken)

                    localStorage.setItem("accessToken", accessToken)
                    store.commit("accessModule/setAccessToken")
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }

}

</script>

<template>

<div class="main">
    <div class="header">
        <HeaderNavbar />
        <ModalLoginForm />                
    </div>
</div>
  
</template>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}  

body {    
    background-color: #f2f2f2;
    font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans, Garuda,Verdana,Tahoma,sans-serif;
    font-weight: 100;
    font-size: 14px;
    line-height: 1.5;    
  }


a {
    color: #cccccc;
    text-decoration: none;
} 

.color-text-try-pro a  {
    color: #fe5621;
}

.color-text-try-pro a:hover {
    color: #ff8a65; 
}

a:hover {
    color: #fff; 
}

</style>
