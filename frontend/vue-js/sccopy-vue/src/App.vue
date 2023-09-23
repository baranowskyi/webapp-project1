<template>    
    <MainLayout />
</template>

<script>

import MainLayout from '@/layouts/MainLayout.vue'

export default {
    name: "App",    
    components: { 
        MainLayout
    },   

    beforeCreate() {       
        this.$store.commit("accessModule/SET_AUTHENTICATION_DATA")   
        this.$store.commit("currentArtist/SET_CURRENT_ARTIST_DATA")      
    },

    mounted() {
        // this.upadateToken()        
    },
    

    methods: {
        // upadateToken() {}        
    }

}

</script>


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

li {
    list-style-type: none
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





.main-content {
  display: table;
  padding-top: 46px;
  padding: 0 30px;
  width: 1240px;
  margin: 0 auto;
  background-color: #ffffff;
}

/************* nav bar artist content **********************/


.main-user-content {
  /* background-color: bisque; */
  margin-top: 20px;
  position: relative;
  margin-bottom: 20px;
  display: flex;  
}

.left-content {
  /* background-color: rgb(182, 182, 182); */
  width: 820px;
  margin-right: 30px;
  position: relative;    
}

.left-content-hide {
  display: none;
}

.spotlight {
  /* background-color: cadetblue; */
  position: relative;
  height: 100px;
  border-bottom: 1px solid #e5e5e5;
}

.recent-track {
  /* background-color: #f2f; */
  margin-bottom: 20px;
  font-size: 20px;
  margin-top: 35px;
}

.artist-tracks {
  /* background-color: #ff8a65; */
  margin-top: 10px;
  position: relative;
  /* border: 1px solid #ccc; */
}

.right-content {
  /* background-color: rgb(135, 135, 135); */
  width: 300px;
  position: relative;  
  border-left: 1px solid #e5e5e5;  
  padding-left: 30px;
  margin-left: 30px;
}

/* NO CONTENT */

.no-content {
    display: block;
    padding-top: 39px;
    text-align: center;
    padding-bottom: 120px;
}

.no-content-img {
    display: block;
    margin: 0 auto;
}

.no-content-text-up {
    font-size: 18px;
    font-weight: 100;    
    margin-top: 20px;
}

.no-content-text-down {
    font-size: 16px;
    font-weight: 100;
    color: #999;    
    margin-top: 8px;
}

</style>
