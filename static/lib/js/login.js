$(document).ready(function(){

  $("#login-form").click(function(){
  $.post("/",
  {
    name: "Donald Duck",
    comment: "Duckburg"
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  }).fail((e)=>{
    alert(e)
  });
  });

});
