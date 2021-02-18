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
        console.log(res);
        if (res.status === 'email_error') {
            $('#display-message').text(`${res.email} already exists!`)
        } else if (res.status === 'ok') {
            $('#display-message').text(`${res.first_name} ${res.last_name} is registered!`)
        }
    });
});

//##############################################################


// $('#login-form').on('submit', (evt) => {
//     evt.preventDefault();

//     const loginInfo = {
//         'email': $('#login_email').val(),
//         'password': $('#login_password').val()
//     }

//     console.log(loginInfo.email)

//     $.post('/api/login', loginInfo, (res) => {
//         console.log(res);
// if (res.status === 'ok') {
// $('#response').text(`${res.first_name} ${res.last_name} is logged in!`)
// } else if (res.status === 'error') {
//     $('#response').text(res.msg)
// }
//         $('#login-form').slideUp()

//     });


// });

// ###############################################################

$('#input-form').on('submit', (evt) => {
    evt.preventDefault();
    // console.log("clicked!")
    const auditionInputs = {
        'industry': $('#industry').val(),
        'callback': $('#callback').val(),
        'date': $('#date').val(),
        'time': $('#time').val(),
        'project_title': $('#project_title').val(),
        'company': $('#company').val(),
        'role': $('#role').val(),
        'casting_office': $('#casting_office').val(),
        'agent': $('#agent').val(),
        'location': $('#location').val(),
        'notes': $('#notes').val(),
    }
    $.post('/???', auditionInputs, (res) => {
        console.log(res);
        // if (res.status === 'email_error') {
        //     $('#display-message').text(`${res.email} already exists!`)
        // } else if (res.status === 'ok') {
        //     $('#display-message').text(`${res.first_name} ${res.last_name} is registered!`)
        // }
    });
});