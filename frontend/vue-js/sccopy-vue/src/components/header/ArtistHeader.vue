<template>
    <div class="artist-header">
        <div class="background-artist preload-content">      
            <img class="background-artist-img" src="#"/>
        </div>
        <div class="artist-info">
            <div class="avatar-profile-block preload-content">
                <img class="avatar-profile-img" src="#" />
                                    
                <div class="edit-avatar-button">
                    <button onclick="" class="avatar-button"><font-awesome-icon icon="fa-solid fa-camera" />&nbsp Update image</button>
                    <div class="dropdown-content-edit-avatar">
                        <a href="#">Replace image</a>
                        <a href="#">Delete image</a>                
                    </div>
                </div>
                
            </div>
            <div class="artist-data"> 
                <div class="nick-name">display_name ({{ currentUser }})                
                    <font-awesome-icon icon="fa-solid fa-circle-check" style="color: #3588d8; background-color: white; border-radius: 50%;" />
                </div>  
                <div class="name-block">
                    <div class="name">first_name</div>
                    <div class="name">last_name</div>                   
                </div>
                <div class="country-city-block">
                    <div class="country-city">city</div>
                    <div class="country-city">country</div>
                </div>
                <div class="pro-user"><font-awesome-icon icon="fa-solid fa-certificate" style="color: #fe5621;" />&nbsp NEXT PRO</div>
            </div>
            
            <div class="edit-background">
                <button onclick="" class="background-button"><font-awesome-icon icon="fa-solid fa-camera" />&nbsp Update image</button>
                <div class="dropdown-content-edit-background">
                    <a href="#">Replace image</a>
                    <a href="#">Delete image</a>                
                </div>
            </div>
            
        </div> 
    </div>         
</template>

<script>

import store from '@/store'

export default {
    data() {
        return {
            
        }
    },
    computed: {
        currentUser() {
            return store.getters["accessModule/getUserName"]
        }
    },
}

</script>

<style>

.preload-content > img
{
  opacity: 0;  
  transition: opacity 1s;
}

.preload-content > img.show-preload-content
{ 
  display: block;
  opacity: 1;
}

/*********************** header artist start *****************************************************/

.artist-header {
  display: flex;       
  width: 1240px;
  height: 260px;
  margin: 0 auto;
}

.background-artist {
  width: 100%;
  height: 100%;
  background: #a3a3a3;
}

.background-artist-img {
  width: auto;
  height: 100%;  
}

.artist-info {
  height: 260px;
  width: inherit;
  padding: 30px;  
  position: absolute;
}

/********************** artist avatar ************************************/

.avatar-profile-block {
  height: 200px;
  width: 200px;  
  overflow: hidden;
  border-radius: 50%;  
  display: flex;
  cursor: pointer;  
}

.avatar-profile-img {
  width: auto;
  height: 100%;
}

.edit-avatar-button {
  position: absolute;
  bottom: 70px;
  left: 65px;  
  /* opacity: 0; */
}

.edit-avatar-button:hover .avatar-button, .avatar-button:focus, .avatar-profile-block:hover .avatar-button {
  opacity: 100%; 
}

.avatar-button {
  display: inline-block;
  position: absolute;
  height: 26px;
  margin: 0;
  padding: 2px 11px 2px 11px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  background-color: #fff;
  cursor: pointer;
  color: #333;
  font-size: 14px;
  line-height: 20px;
  white-space: nowrap;
  font-weight: 100;
  text-align: center;
  vertical-align: initial;
  box-sizing: border-box;
  opacity: 0;
}

.dropdown-content-edit-avatar {
  display: none;
  position: absolute;
  background-color: #ffffff;
  min-width: 132px;    
  z-index: 1; 
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
  border-right: 1px solid #a3a3a3;
  border-left: 1px solid #a3a3a3;
  border-bottom: 1px solid #a3a3a3;
  top: 26px;  
}

.dropdown-content-edit-avatar a {
  color: black;
  padding: 7px 10px;
  text-decoration: none;
  display: block;
  font-size: 14px;
  font-weight: 100;
}

.dropdown-content-edit-avatar a:hover {
  background-color: #ddd;
  color: #fe5621;
}

.show-edit-avatar {
  display: block;  
}


/*************** artist data *************************************/

.artist-data {
  display: block;
  position: absolute;
  left: 270px;
  top: 30px;
}

.nick-name {
  color: #fff;
  font-weight: 100;
  font-size: 24px;
  line-height: 37px;
  padding: 4px 7px;
  background-color: rgba(0,0,0,.8);
  display: table;
}

.name, .country-city {
  margin-top: 4px;
  color: #ccc;
  font-weight: 100;
  padding: 2px 7px 3px;
  font-size: 16px;
  line-height: 1.2;
  background-color: rgba(0,0,0,.8);
  display: table;
}

.name-block, .country-city-block {
  display: flex;  
}

.pro-user {
  margin-top: 4px;
  color: #fff;
  font-weight: 400;  
  padding: 2px 7px 2px;
  font-size: 14px;
  line-height: 1.3;
  background-color: rgba(0,0,0,.8);
  display: table;
}

/****************** edit background ***************************/

.edit-background {
  height: 260px;
  width: 200px;
  display: flex;
  position: absolute;
  right: 0px;
  bottom: 0;
  padding: 34px;
}

.background-button {
  display: inline-block;
  position: absolute;
  height: 26px;
  margin: 0;
  padding: 2px 11px 2px 11px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  background-color: #fff;
  cursor: pointer;
  color: #333;
  font-size: 14px;
  line-height: 20px;
  white-space: nowrap;
  font-weight: 100;
  text-align: center;
  vertical-align: initial;
  box-sizing: border-box;
  opacity: 0;
}

.edit-background:hover .background-button, .background-button:focus {
  opacity: 100%; 
}

.dropdown-content-edit-background {
  display: none;
  position: absolute;
  background-color: #ffffff;
  min-width: 132px;    
  z-index: 1; 
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
  border-right: 1px solid #a3a3a3;
  border-left: 1px solid #a3a3a3;
  border-bottom: 1px solid #a3a3a3;
  bottom: 129px; 
  overflow: hidden; 
}

.dropdown-content-edit-background a {
  color: black;
  padding: 7px 10px;
  text-decoration: none;
  display: block;
  font-size: 14px;
  font-weight: 100;
}

.dropdown-content-edit-background a:hover {
  background-color: #ddd;
  color: #fe5621;
}

.show-edit-background {
  display: block;  
}

/*********************** header artist end *****************************************************/

</style>