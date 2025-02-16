// JavaScript Document
  var btn = document.querySelector('button')
  var dialog = document.querySelector('dialog')

  btn.addEventListener('click', () => {
    dialog.show()
  })

//var btn=document.getElementById('register-button')
var img = document.getElementById("loading");
//img.style.display = "none";
//btn.addEventListener('click', () => {
////    img.show()
//
//  })
img.style.display = "inline";
setTimeout(function() {img.style.display = "none";},2000);

function register() {
            document.getElementById("GFG").style.display
                    = "block";
        }