<template>
    <div class="notification">
        <button class="notification-button">
            <font-awesome-icon icon="fa-solid fa-bell" class="notification-icon"/>
        </button>
    </div>
</template>

<script>
export default {

}
</script>

<style>

.notification-button {
    border: none;
    height: 48px;
    width: 40px;
    cursor: pointer;
    background: transparent;
    font-size: 18px;
}

.notification-icon {     
    color: #c8c8c8;         
}

.notification-button:hover .notification-icon {        
    color: #fff;
}

</style>