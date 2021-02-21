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

    $('.flashes').empty()

    $.post('/api/register', formInputs, (res) => {
        console.log(res);
        if (res.status.code === '200') {
            $('#display-message').text(`${res.first_name} ${res.last_name} is registered!`)
        } else {
            $('#display-message').text(`${res.email} cannot be created!`)
        }
    });
});

// ###############################################################

$('#input-form').on('submit', (evt) => {
    evt.preventDefault();
    console.log("clicked!")
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
    $.post('/input', auditionInputs, (res) => {
        $('#input_page').html(`<p>Your form has been submitted</p>`);
    });
});

//#################################################
$(document).ready(function () {
    $('#callback').change((evt) => {
        evt.preventDefault();
        if ($('#callback').val() === 'yes') {
            $('.job-titles').show();
            $('.audition-form').hide();
        } else if ($('#callback').val() === "no") {
            $('.audition-form').show();
            $('.job-titles').hide();
        }
    })
});

$(document).ready(function () {
    $('.job-titles').click('change', (evt) => {
        console.log(evt.target.value)
        $('#audition').not('[jobid=' + evt.target.value + ']').hide();
        $('.auditions').find('[jobid=' + evt.target.value + ']').show();

        // $('[jobid=' + evt.target.value + ']') ? $(this).show() : $(this).hide()
        // $('.auditions').attr('jobid') === evt.target.value ? $(this).show() : $(this).hide()


        // // grab job-title value (job_id) --> filter audition buttons by job_id
        // // $('.audition-form').show()
        // const formData = {
        //     'job_id': $('#job_title').val()
        // }
        // $.get('/get-auditions', formData, (res) => {
        //     console.log(res)
        // })
    })
});

//##############################################################

// $('#go-feed').on('click', (evt) => {
//     evt.preventDefault();
//     $.get('/feed', (res) => {
//         console.log(res);
//     })
// })

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