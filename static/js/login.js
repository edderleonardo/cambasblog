$(function() {
    console.log( "ready!" );
    let token = sessionStorage.getItem("token");
     if (token != null) {
        window.location.href = '/posts/'
    }
    const login = $('#login');
    const btn_user = $('#btn-new-user');
    const modal = $('#nuevo-usuario-modal');
    const form_register_modal = $('#form-register-modal');

    const country_select = $('#country')
    let username_register = $('#username-register');
    let email_register = $('#email-register');
    let password_register = $('#password-register');
    let name_register = $('#name-register');
    let last_name_register = $('#last-name-register');
    let country = $('#country');
    const btn_register = $('#register');

    const clean_fields = function () {
        email_register.val('');
        password_register.val('');
        name_register.val('');
        last_name_register.val('');
        country.val('');
        country_select.empty()
    };

    login.click(function(e){
        // Btn login
        const email = $('#email').val();
        const password = $('#pass').val();
        const form = $("#login-form");

        e.preventDefault();

        form.parsley().validate();

        if (form.parsley().isValid()){
            const data = {
                "email": email,
                "password": password
            };
            $.ajax({
                type: 'POST',
                url: '/api/login/',
                dataType: 'json',
                data: data,
                success: function(data){
                    sessionStorage.setItem("token", data.token);
                     window.location.href = '/posts/'
                },
                error: function(data){
                    console.log("Error ", data);
                }
            });
        }

    });

    btn_user.click(function(e){
        e.preventDefault();
        const url = '/api/countries/';
        $.getJSON(url, function (data) {
          country_select.append("<option value disabled selected> País* </option>");
          for(var i in data.results) {
            country_select.append("<option value=" + data.results[i].id + ">" + data.results[i].name + "</option>");
          }
        });
        modal.modal('show');
    });

    modal.on('hidden.bs.modal', function (e) {
        clean_fields();
        form_register_modal.parsley().reset();
    });

    btn_register.click(function () {
        form_register_modal.parsley().validate();

        if (form_register_modal.parsley().isValid()) {

            let email_r = email_register.val();
            let pass_r = password_register.val();

            let data = {
                "username": username_register.val(),
                "email": email_r,
                "password": pass_r,
                "name": name_register.val(),
                "last_name": last_name_register.val(),
                "country": country.val()
            };
            const url = '/api/create/user/';
            $.ajax({
                type: "POST",
                url: url,
                data: data,
                success: function (data) {
                    console.log(data);
                },
                error: function (data) {
                    console.log(data);
                }
            });
            modal.modal('hide');
            clean_fields();
            $.notify({
                message: "Su usuario fue creado, ya puede ingresar con sus credenciales"
            }, {
                type: 'success'
            });
        }

    })
});