<script>

import { RouterLink, RouterView } from 'vue-router'
import HeaderNavbar from '@/components/header-navbar/HeaderNavbar.vue'
import ModalLoginForm from '@/components/modal/ModalLoginForm.vue'

export default {
    name: "App",
    components: {
        HeaderNavbar,  
        ModalLoginForm,
    },
    
}

</script>

<template>

<div class="main">
    <div class="header">
        <header-navbar></header-navbar>        
    </div>    
    <modal-login-form></modal-login-form>
    
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
