"use strict";

// #######################REGISTER AND LOGIN####################################

$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
    });

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
            $('#display-message').text(`Hi ${res.first_name} ${res.last_name}! You have successfully created an account. Please Log In!`)
        } else {
            $('#display-message').text(`An account with the email ${res.email} already exists. Please try again with a different email`)
        }
    });
});

//##########################CALLBACK YES OR NO - INPUT.HTML################################################

let selectedProjectId = null;
let callbackInfo = null; 
//creates global variable to hold the auditon id
let audition_id = null;

async function addMedia() {
    const url = "/upload-cloudinary";
    const fileList = document.querySelectorAll("[type=file]");

    //iterate over the media files
    for (let i = 0; i < fileList.length; i++) {
        const formData = new FormData();
      
        let file = fileList[i];
        formData.append("file", file.files[0]);
        //this is where we send the data to the /upload-cloudinary end point
        let cloud_res = await fetch(url, {
            method: "POST",
            body: formData
        })
        //we are waiting for cloudinary to return the media object 
        let cloud_res_json = await cloud_res.json();

        //this is where we store the media in the database
        let flask_resp = await fetch('/submit-media', {
            method: "POST",
            body: JSON.stringify({
                "media_url": cloud_res_json.url,
                "media_title": $(`#media-title-${i+1}`).val(),
                "audition_id" : audition_id,
            }),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        
        if (!flask_resp.ok) {
            alert(`Unable to load files. ${flask_resp.statusText}`)
            break 
        }   
    }
    //once function has completed, we reroute to the feed
    window.location = '/feed'
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
        $('#industry').val(data.industry)
        $('#project_title').val(data.project_title)
        $('#company').val(data.company)
        $('#casting_office').val(data.casting_office)
        $('#agency').val(data.agency)

    })
}

$('#yes').on('click', (evt) => {
    $('.project-titles').show();
    $('#add-media').hide();
    $('#audition-form').hide();
    $('.audition-form').attr('id', 'old-audition-form')
    document.getElementById("old-audition-form").reset();
        const formData = {
            'project_id': $('#project-selector').val()
        }
        $.get('/get-auditions', formData, (res) => {
        })
    })

    $('#project-selector').on('change', (evt) => {
        selectedProjectId = evt.currentTarget.value
        $('.project-titles').hide();
        $('.audition-form').show("fast", autofillProject());
        $('#add-media').show();    
    })

$('#no').on('click', (evt) => {
    $('.audition-form').show();
    $('#add-media').show();
    $('.project-titles').hide();
    $('.audition-form').attr('id', 'new-audition-form')
    document.getElementById("new-audition-form").reset();
})
   
$(document).ready(function () {
    $('.audition').on('click', (evt) => {
    })
});

// ########################IF NOT A CALLBACK - INPUT.HTML#######################################

const form = document.querySelector("#audition-form");

if (form){

form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    // here, we are getting the user input   
    const projectInputs = {
        'industry': $('#industry').val(),
        'project_title': $('#project_title').val(),
        'company': $('#company').val(),
        'casting_office': $('#casting_office').val(),
        'agency': $('#agency').val(),
    };
    const auditionInputs = {
        'date': $('#date').val(),
        'location': $('#autocomplete').val(),
        'role': $('#role').val(),
        'notes': $('#notes').val(),
    };

    //new audtion form means this is NOT a callback for a previously logged project
    if ($('.audition-form').attr('id')==='new-audition-form') {
        //this is where we send data to the backend for the project to be created
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
            //this is where we send data to the backend for the audition to be created
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
            //once all previous data is returned, then we call the addMedia function
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
        .then((data) => {
            audition_id = data.audition_id;
            return data
        }).then(addMedia())
    }
}); //end of long ass function
}

// ###################################GOOGLE MAPS#######################################

var placeSearch, autocomplete;
      var componentForm = {
        street_number: 'short_name',
        route: 'long_name',
        locality: 'long_name',
        administrative_area_level_1: 'short_name',
        country: 'long_name',
        postal_code: 'short_name'
      };

      function initAutocomplete() {
        autocomplete = new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
            {types: ['geocode', 'establishment']});
        }

      function geolocate() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var geolocation = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            var circle = new google.maps.Circle({
              center: geolocation,
              radius: position.coords.accuracy
            });
            autocomplete.setBounds(circle.getBounds());
          });
        }
      }