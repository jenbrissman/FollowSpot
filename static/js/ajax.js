"use strict";
// #######################HOME.HTML####################################


$('#register-form').on('submit', (evt) => {
    evt.preventDefault();
    const formInputs = {
        'first_name': $('#first_name').val(),
        'last_name': $('#last_name').val(),
        'email': $('#email').val(),
        'password': $('#password').val(),
        'phone': $('#phone').val(),
    }

    $('.flashes').empty()

    $.post('/api/register', formInputs, (res) => {
       
        if (res != 'None') {
            $('#display-message').text(`${res.first_name} ${res.last_name} is registered!`)
        } else {
            $('#display-message').text(`An account with the email ${res.email} already exists. Please try again with a different email`)
        }
    });
});

// ########################INPUT.HTML#######################################

$('#audition-form').on('submit', (evt) => {

    const auditionInputs = {
        'industry': $('#industry').val(),
        'callback': $('#callback').val(),
        'date': $('#date').val(),
        'time': $('#time').val(),
        'project_title': $('#project_title').val(),
        'company': $('#company').val(),
        'role': $('#role').val(),
        'casting_office': $('#casting_office').val(),
        'agency': $('#agency').val(),
        'location': $('#location').val(),
        'notes': $('#notes').val(),
        'media_title': $('#media_title').val(),
        'link': $('#link').val(),

    }
    $.post('/input', auditionInputs, (res) => {
    });
});

// CLOUDINARY TEST 
// $(document).ready(function () {
//     console.log(`document is ready, line 51 ${$.fn.cloudinary_fileupload}`)
//     if ($.fn.cloudinary_fileupload !== undefined) {
//         console.log('we in the if ($.fn.cloudinary_fileupload !== undefined)')
//         $("input.cloudinary-fileupload[type=file]").cloudinary_fileupload();
//         console.log($("input.cloudinary-fileupload[type=file]"));
//     } else {
//         console.log('sorry, it wasnt true')
//     }
// });

//##########################################################################


$('#yes').on('click', (evt) => {
    console.log("WE'VE CLICKED YES ON THE BUTTON")
    $('.job-titles').show();
    $('.audition-div').hide(); // want to add an onclick listener for which job button is pressed and then show the audition form
            
    
        const formData = {
            'job_id': $('#job-title').val()
        }

        $.get('/get-auditions', formData, (res) => {
            console.log(res) //[{auditions: {"aud": [list of audition objects]}}] -> getting None rn
        })
    })
    $('.job-button').on('click', (evt) => {
        let buttonValue = evt.currentTarget.value
        console.log(evt.currentTarget.name)
        console.log(buttonValue);
        $('#project_title').innerHTML()
    })
    
$('#no').on('click', (evt) => {
    console.log("WE'VE CLICKED NO ON THE BUTTON")
    $('.audition-div').show();
    $('.job-titles').hide();
})
    


$(document).ready(function () {
    $('.audition').on('click', (evt) => {
        console.log(evt.currentTarget.value)
    })
});
        
        // }
        // $('.media').show();
        // $('[jobid=' + evt.target.value + ']') ? $(this).show() : $(this).hide()
        // $('.auditions').attr('jobid') === evt.target.value ? $(this).show() : $(this).hide()


        // grab job-title value (job_id) --> filter audition buttons by 
        // job_id
        // $('.audition-form').show()
        // const formData = {
        //     'job_id': $('#job_title').val()
        // }
        // $.get('/get-auditions', formData, (res) => {
        //     console.log(res)
        // })


//////////////// JUST TRYING THINGS OUT
// const job_id = $('#job-button).val()

// an action on the form in HTML -> form info will be grabbed by the server using a post request
// <form aciton='/feed' class={{ job_id }} > 
// callback_info = request.form.get("callback_form_stuff")




//##############################################################

