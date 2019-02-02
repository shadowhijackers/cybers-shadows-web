var SURROGATE_PAIR_REGEXP = /[\uD800-\uDBFF][\uDC00-\uDFFF]/g;
  // Match everything outside of normal chars and " (quote character)
var NON_ALPHANUMERIC_REGEXP = /([^\#-~| |!])/g;

$(document).ready(function(){

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

/**
 * Escapes all potentially dangerous characters, so that the
 * resulting string can be safely inserted into attribute or
 * element text.
 * @param value
 * @returns {string} escaped text
 * @link https://github.com/angular/angular.js/blob/v1.3.14/src/ngSanitize/sanitize.js#L435
 */
function encodeEntities(value) {
  return value.
    replace(/&/g, '&amp;').
    replace(SURROGATE_PAIR_REGEXP, function(value) {
      var hi = value.charCodeAt(0);
      var low = value.charCodeAt(1);
      return '&#' + (((hi - 0xD800) * 0x400) + (low - 0xDC00) + 0x10000) + ';';
    }).
    replace(NON_ALPHANUMERIC_REGEXP, function(value) {
      return '&#' + value.charCodeAt(0) + ';';
    }).
    replace(/</g, '&lt;').
    replace(/>/g, '&gt;');
}


function getValueFromCommentsForm(){

  var name = $("#comments-email").val()
  var comment = $("#comments-comment").val()
  return {name: name, comment: comment}

}


function reloadComments(comments){
   clearTheComments();
   for(var commentIdx = 0; commentIdx< comments.length; commentIdx++){

      var comment = comments[commentIdx];
      var nameTAG = '<h4 class="m-2"> '+ encodeEntities(comment.name) +'</h4>'
      var commentTAG = '<pre class="p-2"> '+ encodeEntities(comment.comment) +'</h4>'
      $("#comments-box").append(nameTAG, commentTAG);

   }

}


function clearTheComments(){
  $("#comments-box").empty();
}