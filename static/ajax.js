"use strict";

$('#create_user').on('submit', (evt) => {
    evt.preventDefault();

    const create_user_form_data = {
        'first_name': $('#first_name').val(),
        'last_name': $('#last_name').val(),
        'email': $('#email').val(),
        'password': $('#password').val(),
        'img_url': $('#img_url').val(),
    }

    $.post('/register', create_user_form_data, (res) => {
        console.log(res)
        $('#response_here').text(`${res.first_name} ${res.last_name} is registered!`)
    });

});