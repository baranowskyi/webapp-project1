
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

// get data from Like database
getAjaxLikeData = (trackId, csrftoken) => {
  $.ajax({
    type: "GET",
    url: "/api/track/like/show-likes/" + trackId,
    dataType: 'json',
    cache: false, 
    headers: { "X-CSRFToken": csrftoken }, 
    success: (data) => {           
      for (artist in data) {
        // if active artist has likes             
        if (data[artist]["artist"] == currentUserArtist) {            
          e = document.querySelector("#like-button" + trackId)
          e.classList.add("like-click")
        }
      }
      e = document.querySelector("#like-button-text" + trackId)        
      if (e.textContent == '') {
        e.textContent = e.textContent.replace('', data.length)
      }
      e.textContent = data.length 
    },
    error: (error) => {        
      console.log(error)   
      e = document.querySelector("#like-button-text" + trackId)
      e.textContent = 'Like'    
    }            
  })     
}  

// post and delete data to Like database
editAjaxLikeData = (trackId, artistId, type_request, csrftoken) => {
  $.ajax({
    type: type_request,
    url: "/api/track/like/edit-like/" + trackId,
    dataType: 'json',        
    headers: { "X-CSRFToken": csrftoken },        
    data: { artist: artistId, track: trackId },
    cache: false,
    success: (data) => {        
      getAjaxLikeData(trackId, csrftoken)
    },
    error: (error) => {        
      console.log(error)
    }
  }) 
}  

// catch click like button
document.addEventListener("click", (e) => {      
  if (e.target.classList.contains("like-button")) {
    
    if (currentUser != 'AnonymousUser') {
      // get track ID
      trackId = e.target.id.slice(11)        
      // add like style and count likes + 1
      if (!e.target.classList.contains("like-click")) {        
        e.target.classList.add("like-click")  
      editAjaxLikeData(trackId, artistId, type_request="POST", csrftoken)
      }
      //remove like style and count likes - 1
      else {   
        e.target.classList.remove("like-click")          
      editAjaxLikeData(trackId, artistId, type_request="DELETE", csrftoken)
      }          
    }
    else {
      // show login form
      const modal_login = document.getElementById("modal-login")
      modal_login.style.display = "block"
    }
  }  
})

