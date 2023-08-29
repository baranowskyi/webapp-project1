<template>
<transition name="show-modal-login">  
    <div 
        v-show="getModalStatus"     
        @click="closeModal" 
        @keydown.esc="closeModal"
        tabindex="0"
        ref="modal"    
        class="modal"
    >
        <transition name="show-modal-login-content"> 
            <div v-show="getModalStatus" class="modal-content" @click.stop>
                <div class="modal-header">        
                    <span
                    @click="closeModal" 
                    class="close" 
                    >
                    &times;</span>  
                </div>    
                <div class="modal-body"> 
                    <form @submit.prevent="submitLoginForm">            
                        <div class="welcome-text">Welcome back!</div>  
                        <div v-if="isServerError" class="message-error-form">Ooops! Server error. Try again or later.</div>                                                 
                        <input  
                            :disabled="isShowSpinner"                       
                            v-model="username" 
                            :class="[isUserNameError ? 'input-error': '']" 
                            @input="isUserNameError = false" 
                            class="login-input" 
                            type="text" 
                            name="username" 
                            placeholder="Your Username"
                        /> 
                        <div v-if="isUserNameError" class="message-error-form">Enter a valid Username</div>
                        <Spinner v-if="isShowSpinner"/> 
                        <input    
                            :disabled="isShowSpinner"                    
                            v-model="password" 
                            :class="[isPasswordError ? 'input-error': '']" 
                            @input="isPasswordError = false"
                            class="password-input" 
                            type="password" 
                            name="password" 
                            placeholder="Your Password"
                        />
                        <div v-if="isPasswordError" class="message-error-form">Enter a valid Password</div>
                        <input 
                            :disabled="isShowSpinner"
                            class="submit-button" 
                            type="submit" 
                            value="Sign in"
                        />                  
                    </form> 
                </div>                                      
            </div>
        </transition>
    </div>  
</transition> 
</template>

<script>
import Spinner from '@/components/services/Spinner.vue'

import axios from 'axios'
import store from '@/store'

export default {  
    name: "ModalLoginForm",  
    components: {
        Spinner,
    },  
    
    data() {
        return {
            username: "",    
            password: "",            
            isUserNameError: null,
            isPasswordError: null,
            isShowSpinner: false,
            isServerError: false,
        }        
    }, 
    computed: {
        getModalStatus() { 
            // get focus from close ESC
            this.$nextTick(() => {
                this.$refs.modal.focus()
            })
            return store.getters["headerNavbarActions/getLoginButton"]
        }
    },    
    
    methods: {
        submitLoginForm() {       

            if (this.validateUsername(this.username)) { 
                this.usernameError(false) 
            }
            else { 
                this.usernameError(true) 
            }

            if (this.validatePassword(this.password)) { 
                this.passwordError(false) 
            }
            else { 
                this.passwordError(true) 
            }
            
            if (this.validateUsername(this.username) && this.validatePassword(this.password)) {

                // clear token
                axios.defaults.headers.common["Authorization"] = ''
                localStorage.removeItem("accessToken")
                localStorage.removeItem("refreshToken")

                this.blockModal(true)

                const loginData = {
                    username: this.username,
                    password: this.password,
                }  
            
                // create JWT token
                axios
                    .post(import.meta.env.VITE_API_JWT_CREATE, loginData)
                    .then(response => {
                        
                        console.log(response.data)
                        if (response.status === 200) {
                            const accessToken = response.data.access
                            const refreshToken = response.data.refresh

                            console.log("accessToken = ", accessToken)
                            console.log("refreshToken =", refreshToken)

                            store.commit("accessModule/setAccessToken", accessToken)
                            store.commit("accessModule/setRefreshToken", refreshToken)

                            axios.defaults.headers.common["Authorization"] = "JWT " + accessToken

                            localStorage.setItem("accessToken", accessToken)
                            localStorage.setItem("refreshToken", refreshToken)

                            // get user data
                            axios
                                .get(import.meta.env.VITE_API_JWT_ME, loginData)
                                .then(response => {
                                    console.log(response.data)
                                    if (response.status === 200) {
                                        const userID = response.data.id
                                        const userName = response.data.username

                                        store.commit("accessModule/setIsAuthenticated", true)
                                        store.commit("accessModule/setUserID", userID)
                                        store.commit("accessModule/setUserName", userName)                                      
                                        
                                        this.blockModal(false)
                                    }
                            })
                            .catch(error => {
                                this.isServerError = true
                                this.blockModal(false)
                                console.log(error)
                            })
                        }                    
                })
                .catch(error => {
                    this.isServerError = true
                    this.blockModal(false)
                    console.log(error)
                })                

                //store.commit("headerNavbarActions/setLoginButton", false)
            }
        }, 

        validateUsername(username) {                        
            if (username != '' &&  (/^[A-Za-z0-9-_]{4,20}$/i.test(username))) {
                return true
            }
        },

        validatePassword(password) {
            if (password != '' && (/^[A-Za-z0-9-_!@#$%^&*?]{4,30}$/i.test(password))) {
                return true
            }
        },
       
        closeModal() {   
            if (!this.isShowSpinner) {         
                store.commit("headerNavbarActions/setLoginButton", false)
                this.username = ""
                this.password = ""            
                this.usernameError(false)   
                this.passwordError(false)
                this.isServerError = false
            }                  
        }, 

        usernameError(status) {             
            this.isUserNameError = status
        },

        passwordError(status) {
            this.isPasswordError = status
        },
        
        // block the modal form elements until get data from the server
        blockModal(status) {            
            this.isShowSpinner = status  
        },        

    }  
    
}

</script>

<style scoped>

.show-modal-login-enter-from { opacity: 0; }
.show-modal-login-enter-to { opacity: 1; }
.show-modal-login-leave-from { opacity: 1; } 
.show-modal-login-leave-to { opacity: 0; }
.show-modal-login-enter-active, .show-modal-login-leave-active { transition: all 0.4s; }

.show-modal-login-content-enter-from { top: -500px; }
.show-modal-login-content-enter-to { top: 0px; }
.show-modal-login-content-leave-from { top: 0px; } 
.show-modal-login-content-leave-to { top: -500px; }
.show-modal-login-content-enter-active, .show-modal-login-content-leave-active { transition: all 0.4s; }

.modal {  
    outline: none;  
    position: fixed; 
    z-index: 100; 
    padding-top: 76px; 
    left: 0;
    top: 0;
    width: 100%; 
    height: 100%; 
    overflow: auto; 
    background-color: hsla(0,0%,94.9%,.9);             
}

 .modal-show {
    display: block;
}

.modal-hide {
    display: none;
}

.modal-content {
    position: relative;
    background-color: #ffffff;
    margin: auto;
    padding: 0;  
    width: 550px;
    height: auto;         
}

.close {
    color: #000;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    cursor: pointer;
}

.modal-header {  
    background-color: #ffffff;
    color: #000;
    font-weight: 100;
    font-size: 24px;
    padding-bottom: 15px;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 10px;
}

.modal-body {
    padding: 20px;
}

.welcome-text {
    font-weight: 800;
    color: #000;
    font-size: 32px;
    margin: 0 auto;
    padding: 100px 135px 25px 135px;
}

.login-input {
    font-weight: 400;
    color: #000;
    font-size: 16px;
    margin: 10px;
    padding: 10px;
    width: 490px;
    height: 40px;
}

.password-input {
    font-weight: 400;
    color: #000;
    font-size: 16px;
    margin: 10px;
    padding: 10px;
    width: 490px;
    height: 40px;
}

.submit-button {
    font-weight: 400;
    color: #fff;
    background-color: #ff5500;
    font-size: 16px;
    margin: 10px;
    margin-bottom: 200px;
    padding: 10px;
    width: 490px;
    height: 40px;
    border: 1px solid #ff5500;
    border-radius: 3px;
    cursor: pointer;
}

.message-error-form {
    font-size: 16px;
    color:red;
    margin: 0 10px 0 10px;  
}

.input-error {
    border: 2px solid red; 
    border-radius: 3px;
}

</style>