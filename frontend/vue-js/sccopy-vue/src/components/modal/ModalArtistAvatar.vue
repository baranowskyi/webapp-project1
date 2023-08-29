<template>
    <div id="modal-image-view" class="modal">
            <div class="modal-content">
                <div class="modal-header"> 
                    display_name           
                    <span id="span-image" class="close">&times;</span>       
                    <div class="dropdown-divider-avatar"></div>       
                </div>    
                <div class="modal-body">        
                    <img src="#" />      
                </div>       
            </div>
        </div>
</template>

<script>

</script>

<style scoped>

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

.dropdown-divider-avatar {
  border-bottom: 1px solid #f2f2f2;
  padding: 7px;
}

</style>