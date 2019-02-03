var Routing = (function(){

  function Routing(){

    console.log("Routing module loaded");

  }

  Routing.navigate = function(pathStr){

    window.location.replace(pathStr)

  }

  Routing.getNavParams = function(){

  return window.location.href

  }

  return Routing

}());