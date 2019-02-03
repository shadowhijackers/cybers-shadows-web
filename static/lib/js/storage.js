var Storage = (function(){

    function Storage(){

      console.log("Browser storage system loaded")

    }

    Storage.setItem = function(key, val){

      localStorage.setItem(key, val)

    }

    Storage.getItem = function(key){

     return localStorage.getItem(key)

    }

    return Storage

}())