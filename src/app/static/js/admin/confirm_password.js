$(document).ready(function(){
    function validatePassword() {
        var password = $("#password").val();
        var confirmPassword = $("#confirm_password").val();
        if (password === confirmPassword) {
            $("#submit_button").removeAttr("disabled");
        } else {
            $("#submit_button").attr("disabled", "disabled");
        }
    }

    $("#password, #confirm_password").on('keyup', validatePassword);
});
