(function(){
  let main = document.querySelector("main")
  let screen_height = window.innerHeight
  main.style.height = window.innerHeight +  "px"
  function resize() {
    if(window.innerHeight < 800){
      main.style.height = window.innerHeight +  "px"
    }
  }

  window.onresize = resize

})();