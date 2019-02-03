


$(document).ready(function(){

  if(isAlreadyLogined())Routing.navigate("/comments");

 $("#login-submit").click(function(){

    $.post("/",

        getLoginFormDatas(),

        function(data,status){
           Storage.setItem("userID", data.email)
           Routing.navigate("/comments")
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

