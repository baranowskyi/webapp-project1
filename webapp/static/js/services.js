//------------------------------------- CONSTANTS -----------------------------------------------------//


// page title
const pageTitleText = {
    ArtistAll: `Stream ${getInfoFromURL("artist")} music | Listen to songs, albums, playlists for free on SCCopy`,
    ArtistPopularTracks: `Stream ${getInfoFromURL("artist")} | Listen to top hits and popular tracks online for free on SCCopy`,
    ArtistTracks: `Stream ${getInfoFromURL("artist")} | Listen to tracks online for free on SCCopy`,
    ArtistAlbums: `Stream ${getInfoFromURL("artist")} | Listen to music albums online for free on SCCopy`,
    ArtistPlaylists: `Stream ${getInfoFromURL("artist")} | Listen to music playlists online for free on SCCopy`,
    ArtistReposts: `Listen to ${getInfoFromURL("artist")}'s favorite music online for free on SCCopy`
}

const API_URL_CURRENT_ARTIST_INFO = "/api/current-artist-show-info/"


//------------------------------------- SERVICE FUNCTION -----------------------------------------------//


// get time ago  
function timeAgo(input) {
    const date = (input instanceof Date) ? input : new Date(input)
    const formatter = new Intl.RelativeTimeFormat('en')
    const ranges = {
        years: 3600 * 24 * 365,
        months: 3600 * 24 * 30,
        weeks: 3600 * 24 * 7,
        days: 3600 * 24,
        hours: 3600,
        minutes: 60,
        seconds: 1
    }
    const secondsElapsed = (date.getTime() - Date.now()) / 1000
    for (let key in ranges) {
        if (ranges[key] < Math.abs(secondsElapsed)) {
        const delta = secondsElapsed / ranges[key]
        return formatter.format(Math.round(delta), key)
        }
    }
}


// get dominant color
function getDominantImageColor(id) {        
    let sourceImage = document.querySelector(`#cover-img${id}`)
    let background = document.querySelector(`#audio-container${id}`) 
    let colorThief = new ColorThief()
    // get color palette from cover
    let color = colorThief.getColor(sourceImage)        
    // set the background color
    background.style.backgroundColor = "rgb(" + color + ")"
}


// finds an element ID and puts HTML
// location: beforeBegin, afterBegin, beforeEnd, afterEnd
function getIDPutHTML(elementID, location, HTMLcode) {
    const getElementID = document.querySelector(`#${elementID}`)
    getElementID.insertAdjacentHTML(location, HTMLcode)
}


// finds an element Class and puts HTML
// location: beforeBegin, afterBegin, beforeEnd, afterEnd
function getClassPutHTML(elementClass, location, HTMLcode) {
    const getElementClass = document.querySelector(`.${elementClass}`)
    getElementClass.insertAdjacentHTML(location, HTMLcode)
}


// activate link navbar content
function activateLinkNavbarContent(id) {
    const linkID = document.getElementById(id) 
    linkID.classList.add("navbar-content-left-link-a-active")
}


// get info from url
// http://site/[artist]/[tracktype]
function getInfoFromURL(type) {
    let urlInfo = ""
    if (type === "artist") {
        urlInfo = window.location.pathname.split("/")[1]
    }
    if (type === "tracktype") {
        urlInfo = window.location.pathname.split("/")[2]
        if (!urlInfo) {
            urlInfo = "all"
        }
    }
    return urlInfo
}


// hide all elements left content unless unlessElement
function hideLeftContentElementUnless(unlessElement) {
    const content = document.getElementsByClassName("left-content-inner")
    for (item = 0; item < content.length; item++) {
        content[item].classList.add("left-content-hide")                
    }
    document.querySelector(`.${unlessElement}`).classList.remove("left-content-hide")
}


// get current user info from api
async function getCurrentArtistInfoFromAPI() {
    try{
        const res = await fetch(API_URL_CURRENT_ARTIST_INFO)
        if (res.ok) {
            const data = await res.json()
            getIDPutHTML(
                "currentInfo",
                "afterBegin",
                `${JSON.stringify(data)}`
            )
            // return data
        }        
        console.log("Request Current Artist Data Status = ", res.status)
    }
    catch(err) {
        throw new Error(`Error Get Current Artist Data >>>`, err)
    }
}

// parse json data current user
// async function parseCurrentArtistInfo(key1, key2) {        
//     const parseInfo = await getCurrentArtistInfoFromAPI()
//     if (parseInfo) {
//         if (key1 && !key2) {  
//             return parseInfo[0][key1]
//         }
//         if (key1 && key2) { 
//             return parseInfo[0][key1][key2]
//         } 
//     }    
// }

function parseCurrentArtistInfo(key1, key2) {
    const parseInfo = JSON.parse(document.querySelector("#currentInfo").textContent)    
    // console.log("parseInfo RAW >>> ", parseInfo)    
    if (parseInfo) {
        if (key1 && !key2) {  
            console.log("parseInfo ONE >>>", parseInfo[0][key1])
            return parseInfo[0][key1]
        }
        if (key1 && key2) { 
            console.log("parseInfo TWO >>>", parseInfo[0][key1][key2])
            return parseInfo[0][key1][key2]
        } 
    } 
}



//------------------------------------ preload spinner start ----------------------------------//

// put preload spinner in block
function putPreloadSpinner() {
    getClassPutHTML(
        "artist-header", 
        "afterBegin", 
        `
        <div class="spinner-container">
            <div class="spinner">
                <div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div>
            </div>
        </div> 
    `)
} 

// hide preload spinner
function hidePreloaderSpinner() {
    document.querySelector(".spinner-container").classList.add("hide-spinner")
}

//------------------------------------ preload spinner end ----------------------------------//


// load media image content (target = class or id from <img>)
async function loadImage(target) {
    const imageTarget = document.querySelector(target)
    let img

    const loadImagePromise = new Promise(resolve => {
        img = new Image()
        img.onload = resolve
        img.src = imageTarget.src
    })
 
    await loadImagePromise
    imageTarget.classList.add('show-preload-content')
    console.log(img, "Loaded")
}















