$(document).ready(function(){

 $("#login-submit").click(function(){

    $.post("/",

        getLoginFormDatas(),

        function(data,status){
         window.location.replace("/comments");
        }

    ).fail(function(err){

   alert(err);

 });

 })

});


function getLoginFormDatas(){

 var login_email = $("#login-email").val();
 var login_pass = $("#login-pass").val();
 return {email: login_email, pass: login_pass}

}