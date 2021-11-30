
const destination = ["ourvission-1", "ourvission-2", "ourvission-1",
                        "ourvission-2","ourvission-1","ourvission-2"];

let i=0;
function changedestinationnext(){
    var banner=document.getElementById("slide-photo");
    if(i<destination.length-1){
      i=i+1;
    }
    else{
      i=0;
    }
    console.log(destination[i]);
    document.getElementById("slide-photo").src="./static/images/"+destination[i]+".jpg";
    banner.classList.add("zoom");
    setTimeout(function(){
      banner.classList.remove("zoom");
    },500);

}
function changedestinationprev(){
  var banner=document.getElementById("slide-photo");
    if(i>0){
      i=i-1;
    }
    else{
      i=destination.length-1;
    }
    console.log(destination[i]);
    document.getElementById("slide-photo").src="./static/images/"+destination[i]+".jpg";
    banner.classList.add("zoom");
    setTimeout(function(){
      banner.classList.remove("zoom");
    },500);

}



// our-vission

var btn=document.getElementsByClassName("btn_dot");
var banner=document.getElementById("banner");

btn[0].onclick=function(){
   banner.src="static/images/ourvission-1.jpg";
   animation_our_vision();

   this.classList.add("btn-dot-col");
}

btn[1].onclick=function(){
  banner.src="static/images/ourvission-2.jpg";

  animation_our_vision();
  this.classList.add("btn-dot-col");
}
btn[2].onclick=function(){
  banner.src="static/images/main-photo.jpeg";
  animation_our_vision();

  this.classList.add("btn-dot-col");
}

function animation_our_vision(){
  banner.classList.add("zoom");
  setTimeout(function(){
    banner.classList.remove("zoom");
  },500);
  for(b of btn){
    b.classList.remove("btn-dot-col");
  }

}
