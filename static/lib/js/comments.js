
$(document).ready(function(){

  if(!isAlreadyLogined())Routing.navigate("/");

  $("#comments-form").click(function(){
  $.post("/comments",
  getValueFromCommentsForm(),
  function(data, status){
    reloadComments(data)
    alert("Data: " + data + "\nStatus: " + status);
  }).fail((e)=>{
    alert(e)
  });
  });

});


function getValueFromCommentsForm(){

  var name = Storage.getItem("userID") || ""
  var comment = $("#comments-comment").val()
  return {name: name, comment: comment}

}


function reloadComments(comments){
   clearTheComments();
   for(var commentIdx = 0; commentIdx< comments.length; commentIdx++){

      var comment = comments[commentIdx];
      var nameTAG = '<h4 class="m-2"> '+ Sanitizer.encodeEntities(comment.name) +'</h4>'
      var commentTAG = '<pre class="p-2"> '+ Sanitizer.encodeEntities(comment.comment) +'</pre>'
      $("#comments-box").append(nameTAG, commentTAG);

   }

}


function clearTheComments(){
  $("#comments-box").empty();
}

