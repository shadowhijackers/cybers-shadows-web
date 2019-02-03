function isAlreadyLogined(){

   if(Storage.getItem("userID")){
      return true
   }

   return false
}