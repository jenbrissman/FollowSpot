"use strict";

$('#register-form').on('submit', (evt) => {
    evt.preventDefault();
    // console.log("clicked!")
    const formInputs = {
        'first_name': $('#first_name').val(),
        'last_name': $('#last_name').val(),
        'email': $('#email').val(),
        'password': $('#password').val(),
    }
    $.post('/api/register', formInputs, (res) => {
        console.log(res)
        $('#display-message').text(`${res.first_name} ${res.last_name} is registered!`)
    });
});

//##############################################################


// $('#login-form').on('submit', (evt) => {
//     evt.preventDefault();

//     const

//         $.post('/', formInputs, (res) => {
//             console.log(res)
//             // $('#login-page').text(`${res.email} is logged in!`)
//         });


// });

