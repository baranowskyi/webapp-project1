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
                            v-model="email" 
                            :class="[isEmailError ? 'input-error': '']" 
                            @input="isEmailError = false" 
                            class="email-input" 
                            type="text" 
                            name="email" 
                            placeholder="Your Email"                            
                        /> 
                        <div v-if="isEmailError" class="message-error-form">Enter a valid Email</div>
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
import Spinner from '@/components/services/modules/Spinner.vue'

import { validateEmail, validatePassword } from '@/components/services/functions/authentication/validation.js'
import apiAxios from '@/components/services/functions/authentication/apiAxios.js'
import store from '@/store'

export default {  
    name: "ModalLoginForm",  
    components: {
        Spinner,
    },  
    
    data() {
        return {
            email: "",    
            password: "",            
            isEmailError: null,
            isPasswordError: null,
            isShowSpinner: false,
            isServerError: false,
        }        
    },
    
    watch: {
        email: function () {
            this.email = this.email.toLowerCase()
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
        async loginUser() {

            // clear user data in storage
            localStorage.removeItem("isAuthenticated")
            localStorage.removeItem("accessToken")
            localStorage.removeItem("userData")

            // show spinner
            this.AnimationSpinnerAndBlockModal(true)            

            const loginData = {
                    email: this.email,
                    password: this.password,
                }   

            try {                
                const response = await apiAxios.post(import.meta.env.VITE_API_LOGIN, loginData)                 
                
                localStorage.setItem("isAuthenticated", true)                
                localStorage.setItem("accessToken", response.data.accessToken)                

                const userData = {
                    userID: response.data.user.id,
                    userName: response.data.user.username,
                    userEmail: response.data.user.email,
                }

                localStorage.setItem("userData", JSON.stringify(userData)) 

                // upadet store
                store.commit("accessModule/SET_AUTHENTICATION_DATA")

                // hide spinner
                this.AnimationSpinnerAndBlockModal(false)
            }
            catch (error) {    
                this.isServerError = true
                this.AnimationSpinnerAndBlockModal(false)                            
                console.log(error.status)
            }
        },

        async getCurrentArtistData() {

            this.AnimationSpinnerAndBlockModal(true)

            try {
                const response = await apiAxios.get("api/user/me/")
                console.log(response.data)

            }
            catch (error) {
                this.AnimationSpinnerAndBlockModal(false)
                this.isServerError = true
                console.log(error.status)
            }

        },

        async submitLoginForm() {       

            if (validateEmail(this.email)) { 
                this.emailError(false) 
            }
            else { 
                this.emailError(true) 
            }

            if (validatePassword(this.password)) { 
                this.passwordError(false) 
            }
            else { 
                this.passwordError(true) 
            }
            
            if (validateEmail(this.email) && validatePassword(this.password)) {

                // login user and get token
                await this.loginUser()    
                await this.getCurrentArtistData()            

                store.commit("headerNavbarActions/setLoginButton", false)
                
            }
        },        
       
        closeModal() {   
            if (!this.isShowSpinner) {         
                store.commit("headerNavbarActions/setLoginButton", false)
                this.email = ""
                this.password = ""            
                this.emailError(false)   
                this.passwordError(false)
                this.isServerError = false
            }                  
        }, 

        emailError(status) {             
            this.isEmailError = status
        },

        passwordError(status) {
            this.isPasswordError = status
        },
        
        // block the modal form elements until get data from the server
        AnimationSpinnerAndBlockModal(status) {            
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

.email-input {
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