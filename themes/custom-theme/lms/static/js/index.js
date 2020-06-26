// Register modal
$(document).ready(function($, undefined) {
    $(document).delegate('form', 'submit', function(e) {
		e.preventDefault();
		var $form = $(this);
		var formdata = $form.serializeArray();
		console.log(formdata);
        $.ajax({
                type: "POST",
                url: "create_account",
                data: formdata,
                success: function(result) {
						console.log(result);
						$('#popUpWindow1').hide();
          				$('.modal-backdrop').remove();
                        alert('You have successfully registered!\nPlease login!.');
                },
                error: function(result) {
                        console.log(result);
						if(result.responseJSON['email'])
							alert('Email is already registered!')
						else if(result.responseJSON['username'])
                        	alert('Username is already taken!')
                }
            });
    });
});




 //Email and password validators
    

    function validateEmail(fld,error_msg)
    {
          if(fld.val()=="")
          {
              fld.css("border-color","red");
              error_msg.text("You didn't enter an email");
              return false;
          }
            else if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(fld.val())==false)
        {
            fld.css("border-color","red");
              error_msg.text("Enter a valid email");
              return false;
        }
      fld.css("border-color","skyblue");
        return true;
    }

    
    function validatePassword(fld,error_msg) {
          //var illegalChars = /[\W_]/; // allow only letters and numbers
 
          if (fld.val() == "") {
              fld.css("border-color","red");
              error_msg.text("You didn't enter a password");
              return false;
          } 
      else if (fld.val().length < 3){
              fld.css("border-color","red");
              error_msg.text("Password length must be greater than 3");
            return false;
 
          }
            else if (fld.val().length > 15){
              fld.css("border-color","red");
              error_msg.text("Password length must be less than 15");
            return false;
 
          }
      fld.css("border-color","skyblue");
        return true;
    }



    //On ready
    $(document).ready(function() { 
      // Login Modal
      $("#login-modal-btn").click(function(e) {
      e.preventDefault();
      var val_email=validateEmail($('#modal-email'),$('#email-login-error'));
      var val_pass=validatePassword($('#modal-password'),$('#password-login-error'));
      if(!val_email) $('#email-login-error').show();
      else $('#email-login-error').hide();
      if(!val_pass) $('#password-login-error').show();
      else $('#password-login-error').hide();
      if(val_email && val_pass){
        $('#email-login-error').hide();
        $('#password-login-error').hide();
          $.ajax({
              type: "POST",
              url: "/login_ajax",
              data: { 
                    email: $("#modal-email").val(),
          password: $("#modal-password").val() 
              },
              success: function(result) {
                    window.location=window.location+"courses";
              },
              error: function(result) {
                    console.log(result);
		    if(result.status == 403)
			console.log("403"+ result);
			//window.location=window.location+"courses";
		    else
                    	alert('Email or Password is not correct. Please check!');
              }
            });
        }
      });
      
      // Reset Modal
      $("#reset-modal-btn").click(function(e) {
      e.preventDefault();
      var val_email=validateEmail($('#modal-reset-email'),$('#email-login-error2'));
      if(!val_email) $('#email-login-error2').show();
      else $('#email-login-error2').hide();
      if(val_email){
          $.ajax({
              type: "POST",
              url: "password_reset/",
              data: { 
                    email: $("#modal-reset-email").val()
              },
              success: function(result) {
          		var x = $("#password-reset-success").html();
          		x = x + result.value;
          		$("#password-reset-success").html(x);
                    	$('#loginHelpWindow').hide();
          		$('#popUpWindow').hide();
          		$('.modal-backdrop').remove();
          		$("#password-reset-success").show();
              },
              error: function(result) {
                    	alert('Please check the email you have entered.');
              }
            });
      }
      });
      
     });   



$(window).load(function() {
         if(getParameterByName('next')) {
              $('#login').trigger("click");
         }
      });



 $("#match").hide();
  $("#mismatch").hide();
  $('#register-password, #register-password-confirm').on('keyup', function () {
  if ($('#register-password').val() == $('#register-password-confirm').val()) {
    $("#mismatch").hide();
    $('#match').show();
  } else 
  {
    $("#match").hide();
    $('#mismatch').show();
  }
  if($("#register-password").val().length==0 || $("#register-password-confirm").val().length==0)
  {
  $("#match").hide();
  $("#mismatch").hide();
  }
});







