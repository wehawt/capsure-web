
function login(){
    var message;
        var user_email = document.getElementById("exampleInputEmail1").value;
        var user_password = document.getElementById("exampleInputPassword1").value;

        var data = [
            {"password": user_password, "email": user_email}
        ];

        $.ajax({
        type: "POST",
        url: "/validate",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            message = result.message;
            //console.log(message);
            if(message == "Successfuly logged in"){
                window.location.href="/welcome";
           }
           else{
            window.location.href="/login";
           }
        } 
        });
  }