"use strict";

const searchBar = document.getElementById('searchBar');
const text = document.getElementsByClassName("col-sm-6 col-lg-4 col-xl-3 p-3");

function searchCards(queryString) {
    console.log(Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString)))
    console.log(Object.values(text).map((t) => console.log(t.outerText.toLowerCase())))
    return Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString))
}

searchBar.addEventListener('keyup', (evt) => {
    console.log(evt)
    const searchString = evt.target.value;
    let searchResults = searchCards(searchString.toLowerCase())
    for (let i = 0; i < text.length; i++) {
        searchResults.includes(text[i]) ? text[i].style.display = "none" : text[i].style.display = "block"    
    }
});

function addColorCards() { 
    let titles = document.getElementsByClassName('title');

    for (let i = 0; i < titles.length; i++) {
        const h2 = titles[i].querySelector('h2');

        if (titles[i].innerText === 'Theatre') {

            try {
                h2.style.backgroundColor = '#602E51'
            }
            catch(error) {
            }  
        }
        else if (titles[i].innerText === 'Television') { h2.style.backgroundColor = '#875053' }
        else if (titles[i].innerText === 'Voiceover') { h2.style.backgroundColor = '#B8BEDD' }
        else if (titles[i].innerText === 'Commercial') { h2.style.backgroundColor = '#4E4C67' }
        else if (titles[i].innerText === 'Film') { h2.style.backgroundColor = '7B6D8D' }
        else if (titles[i].innerText === 'Modeling') { h2.style.backgroundColor = '#B28B84' }
        else if (titles[i].innerText === 'Dance') { h2.style.backgroundColor = '66999B' }
        else if (titles[i].innerText === 'Vocal') { h2.style.backgroundColor = 'BCC4DB' }
        else if (titles[i].innerText === 'Instrumental') { h2.style.backgroundColor = 'B9A394' }
        else if (titles[i].innerText === 'Other') { h2.style.backgroundColor = 'fbc4ab' }

    }
}
$(document).ready(addColorCards)
