<template>
    <div class="navbar-content-right">  
            <button v-if="userIsAuthenticated" class="navbar-content-right-button orange-button navbar-content-right-button-insights"><font-awesome-icon icon="fa-solid fa-chart-column" style="color: #fff;" />&nbsp Your Insights</button>          
            <button class="navbar-content-right-button navbar-content-right-button-station"><font-awesome-icon icon="fa-solid fa-tower-cell" />&nbsp Station</button> 
            <button class="navbar-content-right-button navbar-content-right-button-follow orange-button"><font-awesome-icon icon="fa-solid fa-user-plus" style="color: #fff;" />&nbsp Follow</button>           
            <button class="navbar-content-right-button navbar-content-right-button-share"><font-awesome-icon icon="fa-solid fa-share-from-square" />&nbsp Share</button>
            <button v-if="userIsAuthenticated" class="navbar-content-right-button navbar-content-right-button-edit"><font-awesome-icon icon="fa-solid fa-pen" />&nbsp Edit</button>
            <button v-if="userIsAuthenticated" class="navbar-content-right-button navbar-content-right-button-letter"><font-awesome-icon icon="fa-solid fa-envelope" /></button>
            <button v-if="userIsAuthenticated" class="navbar-content-right-button navbar-content-right-button-dots"><font-awesome-icon icon="fa-solid fa-ellipsis" /></button>
        </div>
</template>

<script>

export default {
    name: "ContentNavbarRightMenu",  

    data() {
        return {             
            userIsAuthenticated: false,
                    
        }
    },

    computed: {
        getUserStatus() {
            this.userIsAuthenticated = this.$store.getters["accessModule/IS_AUTHENTICATED"]
        },              
    },

    watch: {
        getUserStatus() {
            this.userIsAuthenticated         
        },        
        
    },
}

</script>

<style>

.navbar-content-right {
    display: flex;
    right: 0;
    position: absolute;
}

.navbar-content-right-button {    
    margin-left: 5px;
    border: 1px solid #e5e5e5;
    border-radius: 3px;
    background-color: #fff;
    cursor: pointer;
    color: #333;
    white-space: nowrap;
    font-weight: 100;
    text-align: center;
    vertical-align: initial;
    box-sizing: border-box;
    font-size: 14px;
    padding: 5px 10px 5px 10px;   
    line-height: 16px;
}

.orange-button {    
    background: #fe5621 ;
    border: 1px solid #fe5621;
    color: #fff;
}

</style>