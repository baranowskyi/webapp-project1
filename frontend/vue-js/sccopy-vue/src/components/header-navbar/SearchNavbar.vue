<template>

<div class="header-section header-middle">
    <form class="search-form" method="GET" action="">
        <input class="search-input" type="text" name="search" :placeholder="[userIsAuthenticated ? 'Search' : 'Search for artists, bands, tracks, podcasts']"/>
        <button class="search-button" type="submit"><font-awesome-icon icon="fa-solid fa-magnifying-glass"/></button>
    </form>
</div>

</template>

<script>

import { userIsAuthenticatedMixin } from '@/mixins'

export default {
    name: "SearchNavBar",
    mixins: [userIsAuthenticatedMixin]
}

</script>

<style>

.search-form {
    position: relative;
    width: 407px;
    margin: 0 auto;
    padding: 10px;
}

.search-input, .search-button {
    border: none;
    outline: none;
    border-radius: 4px;
}

.search-input {
    width: 100%;
    height: 28px; 
    padding-left: 10px; 
    background-color: #e5e5e5; 
}

.search-input:focus {
    background-color: #fff;
}

.search-button {
    height: 28px;
    width: 28px;
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    cursor: pointer;
}

</style>