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


//##########################CALLBACK YES OR NO - INPUT.HTML################################################

let selectedProjectId = null
let callbackInfo = null 
let audition_id = null;

function addMedia() {
    const url = "https://api.cloudinary.com/v1_1/followspotapp/upload";
    const files = document.querySelector("[type=file]").files;
    console.log(files, '+++++FILES+++++')
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        let file = files[i];
        formData.append("file", file);
        formData.append("upload_preset", "pzasmdxy");
        console.log(file, '***** A FILE *****')
        fetch(url, {
            method: "POST",
            body: formData
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(formData.values())
            console.log(data.url)
            return data
        })
        .then((res) => fetch('/submit-media', {
            method: "POST",
            body: JSON.stringify({
                "media_url": res.url,
                "media_title": $(`#media-title-${i+1}`).val(),
                "audition_id" : audition_id,
            }),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }))
        .then((res) => res.json())
        .then((data) => console.log(data))  
    }
}

function autofillProject() {
    let formData = {'project_id': selectedProjectId}
    fetch('/get-callback-info', {
        method: "POST",
        body: JSON.stringify(formData),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then((res) => res.json())
    .then((data) => {
        callbackInfo = data
        console.log(callbackInfo)
        $('#industry').val(data.industry)
        $('#project_title').val(data.project_title)
        $('#company').val(data.company)
        $('#casting_office').val(data.casting_office)
        $('#agency').val(data.agency)

    })
}

$('#yes').on('click', (evt) => {
    console.log("WE'VE CLICKED 'YES' ON THE BUTTON")
    $('.project-titles').show();
    $('.audition-div').hide(); // want to add an onclick listener for which project button is pressed and then show the audition form
    $('.audition-form').attr('id', 'old-audition-form')
    console.log($('.audition-form').attr('id'))
    document.getElementById("old-audition-form").reset();
        const formData = {
            'project_id': $('#project-selector').val()
        }

        $.get('/get-auditions', formData, (res) => {
            console.log(res)
        })
    })

    $('.project-selector').on('change', (evt) => {
        selectedProjectId = evt.currentTarget.value
        console.log(evt.currentTarget.name)
        console.log(selectedProjectId, '+++++++++CURRENT project ID++++++++');
        $('.project-titles').hide();
        $('.audition-div').show("fast", autofillProject());
        console.log($('.audition-form').attr('id'))
        
        // $('#project_title').innerHTML()
    })

    
$('#no').on('click', (evt) => {
    console.log("WE'VE CLICKED 'NO' ON THE BUTTON")
    $('.audition-div').show();
    $('.project-titles').hide();
    $('.audition-form').attr('id', 'new-audition-form')
    console.log($('.audition-form').attr('id'))
    document.getElementById("new-audition-form").reset();

})
   
$(document).ready(function () {
    $('.audition').on('click', (evt) => {
        console.log(evt.currentTarget.value)
    })
});


// ########################IF NOT A CALLBACK - INPUT.HTML#######################################

const mediaUploader = document.querySelector('#media-files')
mediaUploader.addEventListener('change', function(evt) {
  //add an input text box for each media file that the user wants to upload  
})

const form = document.querySelector("#audition-form");

form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    console.log($('.audition-form').attr('id'))
    console.log("SUBMITTED FORM")
    
    const projectInputs = {
        'industry': $('#industry').val(),
        'project_title': $('#project_title').val(),
        'company': $('#company').val(),
        'casting_office': $('#casting_office').val(),
        'agency': $('#agency').val(),
    };
    const auditionInputs = {
        'date': $('#date').val(),
        'time': $('#time').val(),
        'location': $('#location').val(),
        'role': $('#role').val(),
        'notes': $('#notes').val(),
    };

    if ($('.audition-form').attr('id')==='new-audition-form') {
    
        fetch('/submit-project', {
            method: "POST",
            body: JSON.stringify(projectInputs),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
        .then((response) => response.json())
        .then((data) => {
           fetch('/submit-audition', {
            method: "POST",
            body: JSON.stringify({...auditionInputs, 'project_id': data.project_id, 'callback': $('#no').val()}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }) 
        .then((response) => response.json())
        .then((data) => {
            audition_id = data.audition_id;
            return data
        }).then(addMedia())})

    } else if ($('.audition-form').attr('id')==='old-audition-form') {
        fetch('/submit-audition', {
            method: "POST",
            body: JSON.stringify({...auditionInputs, 'project_id': selectedProjectId, 'callback': $('#yes').val()}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
        .then((res) => res.json())
        //   .then((res) => console.log('RESPONSE: ', res))
        .then((data) => {
            audition_id = data.audition_id;
            return data
        }).then(addMedia())
    }
    
});