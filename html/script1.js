function dockerList(){
  var xhml=new XMLHttpRequest();
  xhml.open("GET","http://13.232.124.244/cgi-bin/cas.py");
  xhml.send();
  xhml.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d2").innerHTML= this.responseText;
  }
}
}

function centosLatest(){
  var xhml2=new XMLHttpRequest();
  xhml2.open("GET","http://13.232.124.244/cgi-bin/centos.py");
  xhml2.send();
  xhml2.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d3").innerHTML= this.responseText;
          console.log(this.responseText);
       }
  }
}



function ubuntuLatest(){
  var xhml3=new XMLHttpRequest();
  xhml3.open("GET","http://13.232.124.244/cgi-bin/ubuntu.py");
  xhml3.send();
  xhml3.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d3").innerHTML= this.responseText;
          console.log(this.responseText);
       }
  }
}

function sinaboxLatest(){
  var xhml4=new XMLHttpRequest();
  xhml4.open("GET","http://13.232.124.244/cgi-bin/sinabox.py");
  xhml4.send();
  xhml4.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d3").innerHTML= this.responseText;
          console.log(this.responseText);
       }
  }
}
function rhelLatest(){
  var xhml5=new XMLHttpRequest();
  xhml5.open("GET","http://13.232.124.244/cgi-bin/rhel.py");
  xhml5.send();
  xhml5.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d3").innerHTML= this.responseText;
          console.log(this.responseText);
       }
  }
}
function fedoraLatest(){
  var xhml6=new XMLHttpRequest();
  xhml6.open("GET","http://13.232.124.244/cgi-bin/fedora.py");
  xhml6.send();
  xhml6.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d3").innerHTML= this.responseText;
          console.log(this.responseText);
       }
  }
}
function dockerImages(){
	 var xhml7=new XMLHttpRequest();
  xhml7.open("GET","http://13.232.124.244/cgi-bin/image.py");
  xhml7.send();
  xhml7.onreadystatechange=function(){
  if(this.readyState==4){
  document.getElementById("d4").innerHTML= this.responseText;
          console.log(this.responseText);
       }
  }

}

