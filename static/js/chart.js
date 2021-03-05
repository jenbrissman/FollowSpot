"use strict"
$.get('/charts.json', (res) => {
    const industry = res. 

})


let myChart1 = document.getElementById("myChart").getContext('2d');

let chart1 = new Chart(myChart1, {
    type: 'doughnut',
    data: {
        labels: ['Theatre', 'Television'],
        datasets: [ {
            data: [69, 31],
            backgroundColor: ['#49A9EA', '6A5ACD'],
        }]
    },
    options: {
        title: {
            text: "Number of Auditions by Industry",
            display: true
        }
    }
});