<template>
    <div class="letter">
        <button class="letter-button">
            <font-awesome-icon icon="fa-solid fa-envelope" class="letter-icon"/>
        </button>
    </div>    
</template>

<script>
export default {
    name: "LetterNavbar",

}
</script>

<style>

.letter-button {
    border: none;
    height: 48px;
    width: 40px;
    cursor: pointer;
    background: transparent;
    font-size: 18px;
}

.letter-icon {        
    color: #c8c8c8;
}

.letter-button:hover .letter-icon {        
    color: #fff; 
}

</style>