function AddAccount(){
  var message;

      var user_fname = document.getElementById("fname").value;
      var user_lname = document.getElementById("lname").value;
      var user_email = document.getElementById("inputEmail4").value;
      var user_password = document.getElementById("inputPassword4").value;
      var user_num = document.getElementById("inlineFormInputGroup").value;
      var user_address = document.getElementById("inputAddress").value;
      var user_city = document.getElementById("inputCity").value;
      var user_zipcode = document.getElementById("inputZip").value;

      var data = [
          {"fname_signup": user_fname,
          "lname_signup": user_lname,
          "email_signup": user_email,
          "password_signup": user_password,
          "number_signup": user_num,
          "address_signup": user_address,
          "city_signup": user_city,
          "zipcode_signup": user_zipcode}
      ];

      $.ajax({
      type: "POST",
      url: "/regis",
      data: JSON.stringify(data),
      contentType: "application/json",
      dataType: 'json',
      success: function(result) {
          message = result.message;
          if(message == "Account Created Successfuly"){
              window.location.href="/signin";
         }
         else{
          window.location.href="/signup";
         }
      } 
      });
}



// function createAccount(){
//     var answer = window.confirm("Confirm Signup?");
//     if (answer) {
//       var x = document.getElementById("snackbar");

//       // Add the "show" class to DIV
//       x.className = "show";

//       // After 3 seconds, remove the show class from DIV
//       setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
      
//     }
//     else {
//       //some code
//     }
//   }