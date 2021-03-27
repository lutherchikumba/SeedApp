const value = JSON.parse(document.getElementById('data').textContent);
const data = JSON.parse(value)

console.log(data);
$(document).ready(function() {
    //example cn be found https://leafletjs.com/
    var map = L.map('map').setView([39, -99], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    data.forEach(function(trial){
    // clean data before creating marker
    // have luther set validation to trials
    // learn size for popups
    // create a circle for the marker and set colors based on filter
        L.marker([trial['fields'].latitude, trial['fields'].longitude])
            .addTo(map)
            .bindPopup(chart(trial));
    });
});
// create chart
// pass trial data
// bind to popup
// download chart
    // direc svg to canvas to png
    // html to png might work
function chart(trial){
    var div = d3.create('div')
    var chart = c3.generate({bindto: div,
            data: {columns: [['GSP', 11], ['Radiate', 15]],
            type:'bar',
            labels:true},
            axis:{
                y:{
                    label:{
                        text: 'Yield b/ac',
                        position: 'outer-middle'}},
                x:{
                    type: 'category',
                    categories:['Treatments']}},
            title:{
                text:trial['fields'].crop+" Trial:"+trial['pk']},
            size:{// create variables
                width: 250,
                height: 200}});
    return div.node();
}

var bar = c3.generate({
    bindto: '#barG',
    data: {
    type:'bar',
      columns: [['sample', 30, 200, 150],]
    }
});

var pie = c3.generate({
    bindto: '#pieG',
    data: {
    type:'pie',
      columns: [['data1', 30],['data2', 40], ['data3', 30]]
    }
});