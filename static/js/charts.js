"use strict"


// $.get('/charts.json', (res) => {
//     const dates = res.dates_practiced; // give us a list of dates
//     // ["Feb 28", "Feb 27", "Feb 26", "Feb 25", "Feb 24", "Feb 23", "Feb 22"]
//     const practiceTimes = res.minutes_practiced; // associated practice minutes only
//     // [0, 0, 120, 12, 45, 35, 100]



let labels1 = ['Theatre', 'Television', 'Film', 'Commercial', 'Voiceover', 'Instrumental', 'Vocal', 'Dance', 'Modeling', 'Other'];
let data1 = [69, 31];
let colors1 = ['#49A9EA', '6A5ACD', '0000FF', 'FFA500', '3CB371', 'EE82EE', '#FF6347', '#36CAAB', '#34495E', '#B370CF'];

let myDoughnutChart = document.getElementById("myChart").getContext('2d');

let chart1 = new Chart(myDoughnutChart, {
    type: 'doughnut',
    data: {
        labels: ['Theatre', 'Television', 'Film', 'Commercial', 'Voiceover', 'Instrumental', 'Vocal', 'Dance', 'Modeling', 'Other'],
        datasets: [ {
            data: [69, 31],
            backgroundColor: ['#49A9EA', '#36CAAB']
        }]
    },
    options: {
        title: {
            text: "Number of Auditions by Industry",
            display: true
        },
        legend : {
            display: false
        }
    }
});