<template>

<div class="container-header-navbar">
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
    
    <SearchNavbar />

    <div class="header-section header-right">            
        <div class="header-item-right color-text-try-pro"><a href="#">Try Next Pro</a></div>
        <div class="header-item-right"><a href="#">For Artists</a></div>
        <div v-if="!userIsAuthenticated" @click.prevent="showLoginModal" class="login-button sign-in-button"><a href="#" >Sign in</a></div>        
        <div v-if="!userIsAuthenticated" class="create-account-button"><a href="#">Create account</a></div>
        <div @click.prevent="showUpload" class="header-item-right"><a href="#">Upload</a></div> 
    </div> 
    
    <!-- profile navbar -->
    <div :class="[isShowProfileMenu ? 'profile-navbar-color': '']" class="profile-navbar">          
        <div class="photo-navbar">
            <img class="photo-navbar-img" :src="AvatarImageSmall">
        </div>        
        <button 
        @click.prevent="showProfileMenu" 
        class="profile-button"
        @keydown.esc="closeProfileMenu"
        tabindex="0"
        ref="profileButton"    
        >
            <font-awesome-icon icon="fa-solid fa-chevron-down" class="arrow-icon"/>
        </button>
        <div v-show="isShowProfileMenu" class="dropdown-content-profile-navbar show-profile-navbar">
            <ul>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-user" />&nbsp Profile</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-heart" />&nbsp Likes</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-folder-open" />&nbsp Playlists</a></li>          
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-tower-cell" />&nbsp Stations</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-users" />&nbsp Following</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-user-group" />&nbsp Who to follow</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-star" />&nbsp Try Next Pro</a> </li>                      
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-gift" />&nbsp Partner offers</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-signal" />&nbsp Tracks</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-chart-column" />&nbsp Insights</a></li>
                <li><a href="#"><font-awesome-icon icon="fa-solid fa-arrow-up-from-bracket" />&nbsp Distribute</a></li>
            </ul>
        </div>
    </div>

    <NotificationNavbar />

    <LetterNavbar />

    <!-- dotting navbar -->
    <div :class="[isShowDottingsMenu ? 'dotting-navbar-color': '']" class="dotting-navbar">     
        <div class="dotting-button">       
            <button 
            @click.prevent="showDottingsMenu"
            class="dot-button"
            @keydown.esc="closeDottingsMenu"
            tabindex="0"
            ref="dotButton"
            >
                <font-awesome-icon icon="fa-solid fa-ellipsis" class="dotting-icon"/>
            </button>
        </div>
        <div :class="[isShowDottingsMenu ? 'show-dotting-navbar' : '']" class="dropdown-content-dotting-navbar">
            <ul>
                <li><a href="#">About us</a></li>
                <li><a href="#">Legal</a></li>
                <li><a href="#">Copyrigth</a></li>
                <div class="dropdown-divider"></div>
                <li><a href="#">Mobile apps</a></li>
                <li><a href="#">For Creators</a></li>
                <li><a href="#">Blog</a></li>
                <li><a href="#">Jobs</a></li>
                <li><a href="#">Developers</a></li>
                <div class="dropdown-divider"></div>
                <li><a href="#">Support</a></li>
                <li><a href="#">Keyboard shortcuts</a></li>                
                <li><a href="#">Subscription</a></li>
                <li><a href="#">Settings</a></li>
                <li><a href="#">Pro plans</a></li>
                <div class="dropdown-divider"></div>
                <li><a href="#">Sign out</a></li>
            </ul>
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
    
    data() {
        return {
            isShowProfileMenu: false,
            isShowDottingsMenu: false,  
            userIsAuthenticated: false, 
            AvatarImageSmall: null,         
        }
    },

    computed: {
        getUserStatus() {
            this.userIsAuthenticated = this.$store.getters["accessModule/IS_AUTHENTICATED"]
        },
        getAvatar() {
            this.AvatarImageSmall = this.$store.getters["currentArtist/AVATAR_IMAGE_SMALL"]    
            
        },        
    },

    watch: {
        getUserStatus() {
            this.userIsAuthenticated         
        },
        getAvatar() {            
            this.AvatarImageSmall            
        },
        
    },
    

    mounted() {
        // close the menu after click outside 
        window.addEventListener("click", event => {
            if (!this.$el.contains(event.target)) {
                this.isShowDottingsMenu = false
                this.isShowProfileMenu = false
            }
        })        
    }, 
    
    
    methods: { 
        showLoginModal() {
            this.$store.commit("modalForm/SET_LOGIN_MODAL_FORM", true)            
        }, 

        showUpload() {
            if (!this.userIsAuthenticated) {
                this.showLoginModal()
            }
        },
        
        showProfileMenu() {
            this.isShowProfileMenu = !this.isShowProfileMenu
            this.isShowDottingsMenu = false
            this.$nextTick(() => {
                this.$refs.profileButton.focus()
            })
            return this.isShowProfileMenu
        },

        closeProfileMenu() {
            this.isShowProfileMenu = false
        },
               
        showDottingsMenu() {
            this.isShowDottingsMenu = !this.isShowDottingsMenu
            this.isShowProfileMenu = false
            this.$nextTick(() => {
                this.$refs.dotButton.focus()
            })
            return this.isShowDottingsMenu
        }, 

        closeDottingsMenu() {
            this.isShowDottingsMenu = false
        },      
       
    } 
}
</script>

<style>

.top-header-navbar {
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

.container-header-navbar {
    display: flex; 
    width: 1240px;
    margin: 0 auto;
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
    padding-top: 4px;
    padding-left: 10px;
    padding-right: 10px;
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
    outline: none;
}

.arrow-icon { 
    color: #c8c8c8;
    margin-left: 31px;
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

.dotting-navbar-color {
    background-color: #111;
}

.dot-button {
    padding: 10px;
    border: none; 
    height: 47px;
    width: 50px; 
    cursor: pointer;
    background: transparent;  
    outline: none;
    font-size: 25px;
}

.dotting-icon { 
    color: #c8c8c8;
}

.dot-button:hover .dotting-icon {        
    color: #fff;
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

