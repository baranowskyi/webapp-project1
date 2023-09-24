<template>
    <div class="no-content">
        <img class="no-content-img" src="@/assets/media/no-content/404-oh-no-page.png"/>
        <span class="no-content-text-up">
            We can’t find that page.
        </span>
        <span class="no-content-text-down">
            A report has been sent to our tech team, and they’re looking into the problem. Please check back in a bit.
        </span>
        <button class="button">I need help</button>
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
                <a><li>Artist Resources </li></a>
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
    </div>

</template>

<script>

</script>

<style scoped>
.no-content {
    display: grid;
    padding-top: 39px;
    text-align: center;
    padding-bottom: 120px;
}

.no-content-img {
    display: block;
    margin: 0 auto;    
}

.no-content-text-up {
    font-size: 28px; 
    margin: 0 auto; 
    margin-top: 50px;
    width: 50%;
}

.no-content-text-down {
    font-size: 18px;    
    color: #999;
    margin: 0 auto;
    margin-top: 10px;
    width: 31%;    
}

.button {
    margin: 0 auto;
    margin-top: 30px;    
    padding: 2px 11px 2px 10px;
    border: 1px solid #e5e5e5;
    border-radius: 3px;
    background-color: #fff;
    cursor: pointer;
    color: #333;
    font-size: 14px;
    line-height: 20px;    
    font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;
    font-weight: 100;
    text-align: center;
}

.button:hover {
    border: 1px solid #c7c7c7;
}

.line {
    border-top: 1px solid #f2f2f2;    
    margin-top: 30px
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