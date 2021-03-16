"use strict";
// console.log($('.title').text())
// console.log($('.card_red').css('background'))
// console.log($('.title').text() === "Television")
// console.log($('.fa').css('background')

const searchBar = document.getElementById('searchBar');
const text = document.getElementsByClassName("col-sm-6 col-lg-4 col-xl-3 p-3");

function searchCards(queryString) {
    console.log(Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString)))
    console.log(Object.values(text).map((t) => console.log(t.outerText.toLowerCase())))
    return Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString))
}

// $(document).ready(searchCards)

searchBar.addEventListener('keyup', (evt) => {
    console.log(evt)
    const searchString = evt.target.value;
    let searchResults = searchCards(searchString.toLowerCase())
    for (let i = 0; i < text.length; i++) {
        searchResults.includes(text[i]) ? text[i].style.display = "none" : text[i].style.display = "block"    
    }
});

// function doFilter(value) {
//     console.log("doFilter: " + value);
//     $("#myTable tr").filter(function() {
//       $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
//     });
//   }

// function filterCards(queryString) {
//     Object.values(text).filter((t) => t.classList.toggle($(this).text().toLowerCase().indexOf(queryString) > -1)
// }

// $(document).ready(function() {
//     $("#searchBar").on("keyup", function() {
//       filterCards($(this).val().toLowerCase());
//     });
// });

// $("#searchBar").autocomplete({
//     source: Object.values(text),
//     close: function(event, ui) {
//       console.log("close");
//       filterCards($("#searchBar").val().toLowerCase());
//     }
// });


// let auditionSearch = user.auditions;


// searchBar.addEventListener("keyup", e => {
//     const searchString = e.target.value;
//     const filteredCharacters = hpCharacters.filter(character => {
//       return (
//         character.name.includes(searchString) ||
//         character.house.includes(searchString)
//       );
//     });
//     displayCharacters(filteredCharacters);
//   });


function addColorCards() { 
    let titles = document.getElementsByClassName('title');
    // console.log(titles)
    // console.log(titles.length)

    for (let i = 0; i < titles.length; i++) {
        const h2 = titles[i].querySelector('h2');
        // console.log('line 20', h2)
        if (titles[i].innerText === 'Theatre') {
            // console.log('line35') 
            // console.log(titles[i])
            try {
                h2.style.backgroundColor = '#E3b5A4'
            }
            catch(error) {
                // console.warn('line 39', error)
            }
            
            // console.log('line37')
        }

        else if (titles[i].innerText === 'Television') { h2.style.backgroundColor = '#875053' }
        else if (titles[i].innerText === 'Voiceover') { h2.style.backgroundColor = '#A3B4A2' }
        else if (titles[i].innerText === 'Commercial') { h2.style.backgroundColor = '#4E4C67' }
        else if (titles[i].innerText === 'Film') { h2.style.backgroundColor = '9EB3C2' }
        else if (titles[i].innerText === 'Modeling') { h2.style.backgroundColor = '#C3A995' }
        else if (titles[i].innerText === 'Dance') { h2.style.backgroundColor = '66999B' }
        else if (titles[i].innerText === 'Vocal') { h2.style.backgroundColor = 'BCC4DB' }
        else if (titles[i].innerText === 'Instrumental') { h2.style.backgroundColor = 'B9A394' }
        else if (titles[i].innerText === 'Other') { h2.style.backgroundColor = 'fbc4ab' }
        // other color options in the theme: 602E51
        // console.log(titles.length, 'length*******')
    }
}

$(document).ready(addColorCards)
