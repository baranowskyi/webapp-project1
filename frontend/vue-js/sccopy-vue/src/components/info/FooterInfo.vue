<template>

    <span class="line"></span>
    <div class="links">
        <ul>
            <a><li>Legal</li></a>
            ⁃ 
            <a><li>Privacy</li></a>
            ⁃ 
            <a><li>Cookie Policy</li></a>
            ⁃ 
            <a><li>Consent Manager</li></a>
            ⁃ 
            <a><li>Imprint</li></a>
            ⁃ 
            <a><li>Artist Resources</li></a>
            ⁃ 
            <a><li>Blog</li></a>
            ⁃ 
            <a><li>Charts</li></a>
            ⁃
        </ul>
    </div>

    <div class="language">
        <a class="a-language">Language:</a>
        <span>English (US)</span>
    </div>

</template>

<style scoped>

.line {
    border-top: 1px solid #f2f2f2;    
    margin-bottom: 20px;
    display: flex;
}

.links {
    margin-top: 10px;
    display: flex;
    font-size: 12px;
    color: #ccc;
}

li {
    display: contents;
}

a:hover {
    cursor: pointer;
    color: #a1a1a1;
}

.language {
    margin-top: 5px;;
    display: flex;
    font-size: 12px;
    width: 140px;
}

.language:hover {
    cursor: pointer;
}

.a-language {
    color: #38d;
    margin-right: 5px;
}

.language:hover .a-language {
    color: black
} 

</style>