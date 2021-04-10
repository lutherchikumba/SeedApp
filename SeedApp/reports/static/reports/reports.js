
const data_value = JSON.parse(document.getElementById('data').textContent);
const data = JSON.parse(data_value);



$(document).ready(function() {
    //example cn be found https://leafletjs.com/
    var map = L.map('map').setView([39, -99], 4);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    data.forEach(function(trial){
    // learn size for popups
    // create a circle for the marker and set colors based on filter
        L.marker([trial.lat, trial.lng])
            .addTo(map)
            .bindPopup(chart(trial));
    });
});

// download chart
// direc svg to canvas to png
// html to png might work
function chart(trial){
    var div = d3.create('div');
    var values = [];
    var names = Array(trial.measures.length).fill('');
    trial.products.forEach(function(product){
            names[product.treatment-1] += product.product;
    });
    trial.measures.forEach(function(measure){
        values.push([names[measure.treatment-1], measure.value]);
    });
    var chart = c3.generate({bindto: div,
            data: {columns: values,
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
                text:trial.crop+" Trial:"+trial.id},
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

// get the selected filters
$('#id_countries, #id_crops ,#id_products').change(function(){
    var country = $('#id_countries').val();
    var products = $('#id_crops').val();
    var products = $('#id_products').val();
    console.log(country, products);
    console.log(data);
    //filter data
    //
});