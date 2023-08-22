<template>
<div :class="{'modal-show': modalVisible}" id="modal-login" class="modal">    
    <div class="modal-content">
        <div class="modal-header">        
            <span @click="closeModal" id="span-login" class="close">&times;</span>  
        </div>    
        <div class="modal-body">  

        <form @submit.prevent="submitLoginData">
            
            <div class="welcome-text">Welcome back!</div>
            <div>                
                <input v-model="username" class="login-input" type="text" name="username" placeholder="Your Username"/>
            </div>
            <div> 
                <input v-model="password" class="password-input" type="password" name="password" placeholder="Your Password"/>
            </div>
            <div>
                <input class="submit-button" type="submit" value="Sign in"/>
            </div>
            
        </form>                

        </div>       
    </div>
</div>  
</template>

<script>

export default {      

    name: "ModalLoginForm",
    data() {
        return {
            username: "",    
            password: "",
            modalVisible: false,
        }        
    },
    methods: {
        async submitLoginData() {
            const loginData = {
                username: this.username,
                password: this.password,
            }
            await fetch(`${import.meta.env.VITE_MAIN_URL}/login`, {
                method: "POST",
                headers: { "Content-Type": "applicatin/json" },
                credentials: "include",
                body: JSON.stringify(loginData)
            })            
        },
        closeModal() {
            this.modalVisible = false
            // clearError()
        }
    }
}

</script>

<style>

.modal {
    display: none; 
    position: fixed; 
    z-index: 999; 
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

.modal-content {
    position: relative;
    background-color: #ffffff;
    margin: auto;
    padding: 0;  
    width: 550px;
    height: auto;  
    -webkit-animation-name: animatetop;
    -webkit-animation-duration: 0.4s;
    animation-name: animatetop;
    animation-duration: 0.4s
    }

@-webkit-keyframes animatetop {
    from {top:-300px; opacity:0} 
    to {top:0; opacity:1}
}

@keyframes animatetop {
    from {top:-300px; opacity:0}
    to {top:0; opacity:1}
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