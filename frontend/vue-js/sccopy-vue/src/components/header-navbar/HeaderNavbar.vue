<template>

<div class="container-header-bar">
    <!-- site logo -->
    <div class="header-logo">
        <a href="#">
            <font-awesome-icon icon="fa-brands fa-soundcloud" class="logo-icon"/>
        </a>
    </div>

    <div class="header-section header-left">  
        <div class="header-item"><a href="#">Home</a></div>
        <div class="header-item"><a href="#">Feed</a></div>
        <div class="header-item"><a href="#">Library</a></div>
    </div>
    
   <!-- search --> 
   <search-navbar></search-navbar>

    <div class="header-section header-right">            
        <div class="header-item-right color-text-try-pro"><a href="#">Try Next Pro</a></div>
        <div class="header-item-right"><a href="#">For Artists</a></div>            
        <div 
            @click.prevent="showLoginModal" 
            class="login-button sign-in-button"
            >
            <a href="#" >Sign in</a>
        </div>
        <div class="create-account-button"><a href="#">Create account</a></div>
        <div class="header-item-right"><a href="#">Upload</a></div> 
    </div> 
    
    <!-- profile navbar -->
    <div class="profile-navbar">          
        <div class="photo-navbar"><img class="photo-navbar-img" src=""></div>        
        <button 
        @click.prevent="profileDropMenu"
        class="profile-button"
        >
            <font-awesome-icon icon="fa-solid fa-chevron-down" class="arrow-icon"/>
        </button>
        <div class="dropdown-content-profile-navbar">
            <a href="#"><font-awesome-icon icon="fa-solid fa-user" />&nbsp Profile</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-heart" />&nbsp Likes</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-folder-open" />&nbsp Playlists</a>            
            <a href="#"><font-awesome-icon icon="fa-solid fa-tower-cell" />&nbsp Stations</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-users" />&nbsp Following</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-user-group" />&nbsp Who to follow</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-star" />&nbsp Try Next Pro</a>                       
            <a href="#"><font-awesome-icon icon="fa-solid fa-gift" />&nbsp Partner offers</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-signal" />&nbsp Tracks</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-chart-column" />&nbsp Insights</a>
            <a href="#"><font-awesome-icon icon="fa-solid fa-arrow-up-from-bracket" />&nbsp Distribute</a>
        </div>
    </div>

    <!-- notification navbar -->
    <notification-navbar></notification-navbar>

    <!-- letter navbar -->
    <letter-navbar></letter-navbar>

    <!-- dotting navbar -->
    <div class="dotting-navbar">     
        <div class="dotting-button">       
            <button 
            @click.prevent="dottingDropMenu"
            class="dot-button"
            >
            </button>
        </div>
        <div class="dropdown-content-dotting-navbar">
            <a href="#">About us</a>
            <a href="#">Legal</a>
            <a href="#">Copyrigth</a>
            <div class="dropdown-divider"></div>
            <a href="#">Mobile apps</a>
            <a href="#">For Creators</a>
            <a href="#">Blog</a>
            <a href="#">Jobs</a>
            <a href="#">Developers</a>
            <div class="dropdown-divider"></div>
            <a href="#">Support</a>
            <a href="#">Keyboard shortcuts</a>                 
            <a href="#">Subscription</a>
            <a href="#">Settings</a>
            <a href="#">Pro plans</a> 
            <div class="dropdown-divider"></div>
            <a href="#">Sign out</a>
        </div>
    </div>
</div> 


</template>


<script >
import SearchNavbar from '@/components/header-navbar/SearchNavbar.vue'
import NotificationNavbar from '@/components/header-navbar/NotificationNavbar.vue'
import LetterNavbar from '@/components/header-navbar/LetterNavbar.vue'


export default {   
    name: "HeaderNavbar", 
    components: {
        SearchNavbar,
        NotificationNavbar,
        LetterNavbar,
         
    },
    methods: {
        profileDropMenu() {
            document.querySelector(".profile-navbar").classList.toggle("profile-navbar-color")
            document.querySelector(".dropdown-content-profile-navbar").classList.toggle("show-profile-navbar")
        },
        dottingDropMenu() {
            document.querySelector(".dropdown-content-dotting-navbar").classList.toggle("show-dotting-navbar")
        },
        showLoginModal() {
            document.getElementById("modal-login").style.display = "block" 
        }
    } 
}
</script>

<style>

.container-header-bar {
    display: flex; 
    width: 1240px;
    margin: 0 auto;
}    

.header {
    display: flex;
    justify-content: space-between;    
    background-color: #333333;   
    height: 46px;    
    align-items: center; 
    margin: 0 auto; 
    position: sticky;
    z-index: 3;
    top: 0;
}

.header-item {
    display: block;
    padding: 12px 0;
    height: 46px;
    box-sizing: border-box;
    text-align: center;
    width: 104px;
    border-right: 1px solid #111;
}

.header-section {
    display: flex;
    align-items: center;
}

.header-logo {
    background: #111;
    height: 46px;
    width: 70px;
    text-align: center;
}

.logo-icon {
    color: #ffffff; 
    font-size: 38px; 
    padding-top: 5px;
}

.header-left {
    padding-left: 0px;
}

.header-right {    
    white-space: nowrap;
}

.header-item-right {
    display: block;
    padding: 12px 10px;
    height: 46px;    
    text-align: center; 
}

.sign-in-button {
    background-color: #333333;
    border-radius: 3px;
    padding: 3px 15px 3px 15px;
    margin-left: 10px;
    margin-right: 10px;
    border: 1px solid #a3a3a3;  
    cursor: pointer; 
}

.sign-in-button:hover {
    border: 1px solid #e5e5e5;
}

.create-account-button {  
    background-color: #ff5500;
    border-radius: 3px;
    padding: 3px 15px 3px 15px;
    margin-left: 10px;
    margin-right: 10px;
    cursor: pointer;  
}

.sign-in-button a, .create-account-button a {
    color: #ffffff;
}

/*********************** profile button start *****************************************************/

.profile-navbar {
    height: 47px;
    width: 58px;
    display: flex;
}

.profile-navbar-color {
    background-color: #111;
}

.photo-navbar {
    width: 26px;
    height: 26px;
    overflow: hidden;
    border-radius: 50%;
    margin: 11px;
    margin-right: 3px;
}

.photo-navbar-img {
    width: auto;
    height: 100%;
}

.profile-button {
    padding: 10px;
    border: none; 
    height: 48px;
    width: 55px; 
    cursor: pointer;
    background: transparent;
    position: absolute;
}

.arrow-icon { 
    color: #c8c8c8;
}

.profile-button:hover .arrow-icon {        
    color: #fff;
}

.dropdown-content-profile-navbar {
    display: none;
    position: absolute;
    background-color: #ffffff;
    min-width: 135px;    
    z-index: 1;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    border-right: 1px solid #a3a3a3;
    border-left: 1px solid #a3a3a3;
    border-bottom: 1px solid #a3a3a3;
}

.dropdown-content-profile-navbar a {
    color: black;
    padding: 7px 10px;
    text-decoration: none;
    display: block;
    font-size: 12px;
    font-weight: 700;
}

.dropdown-content-profile-navbar a:hover {
    background-color: #ddd;
    color: #000;
}

.show-profile-navbar {
    display: block;
    margin-top: 47px;
}

/*********************** profile end start *****************************************************/





/*********************** dotting button start *****************************************************/

.dot-button {
    padding: 10px;
    border: none; 
    height: 47px;
    width: 50px; 
    cursor: pointer;
    background: transparent;  
}

.dot-button:focus {
    background: center / contain no-repeat url(../../assets/media/dot-icon-on-active.svg);
} 

.dotting-button {  
    background: center / contain no-repeat url(../../assets/media/dot-icon-off.svg);
}

.dotting-button:hover {  
    background: center / contain no-repeat url(../../assets/media/dot-icon-on.svg);
}  

.dotting-navbar {
    position: relative;
    display: inline-block;
}

.dotting-navbar a:hover {
    background-color: #ddd;
    color: #000;
}

.dropdown-content-dotting-navbar {
    display: none;
    position: absolute;
    background-color: #ffffff;
    min-width: 160px;    
    z-index: 1;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    border-right: 1px solid #a3a3a3;
    border-left: 1px solid #a3a3a3;
    border-bottom: 1px solid #a3a3a3; 
    right: 0;
}

.dropdown-content-dotting-navbar a {
    color: black;
    padding: 7px 10px;
    text-decoration: none;
    display: block;
    font-size: 12px;
    font-weight: 700;
}

.dropdown-divider {
    border-bottom: 1px solid #f2f2f2;
}

.show-dotting-navbar {
    display: block;
}


/*********************** dotting button end *****************************************************/

</style>

