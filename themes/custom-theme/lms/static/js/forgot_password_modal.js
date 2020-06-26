(function() {
    $(document).delegate('#pwd_reset_form', 'ajax:success', function(data, json, xhr) {
      if(json.success) {
        $("#password-reset").text(json.value);
      } else {
        if($('#pwd_error').length == 0) {
          var msg = "${_("Email is incorrect.") | n, js_escaped_string}";
          var error_msg = HtmlUtils.interpolateHtml(
          edx.HtmlUtils.HTML('<div id="pwd_error" class="modal-form-error">{error_msg}</div>'),
          {
            error_msg: msg,
          });
          $('#pwd_reset_form').prepend(edx.HtmlUtils.ensureHtml(error_msg).toString());
        }
        $('#pwd_error').stop().css("display", "block");
      }
    });

    // removing close link's default behavior
    $('#login-modal .close-modal').click(function(e) {
     e.preventDefault();
    });

    var onModalClose = function() {
      $("#forgot-password-modal").attr("aria-hidden", "true");
      $("#forgot-password-link").focus();
    };

    var cycle_modal_tab = function(from_element_name, to_element_name) {
      $(from_element_name).on('keydown', function(e) {
          var keyCode = e.keyCode || e.which;
          var TAB_KEY = 9;  // 9 corresponds to the tab key
          if (keyCode === TAB_KEY) {
              e.preventDefault();
              $(to_element_name).focus();
          }
      });
    };
    $("#forgot-password-modal .close-modal").click(onModalClose);
    cycle_modal_tab("#forgot-password-modal .close-modal", "#pwd_reset_email");
    cycle_modal_tab("#pwd_reset_email", "#pwd_reset_button");
    cycle_modal_tab("#pwd_reset_button", "#forgot-password-modal .close-modal");

    // Hitting the ESC key will exit the modal
    $("#forgot-password-modal").on("keydown", function(e) {
        var keyCode = e.keyCode || e.which;
        // 27 is the ESC key
        if (keyCode === 27) {
            e.preventDefault();
            $("#forgot-password-modal .close-modal").click();
        }
    });

  })(this)
