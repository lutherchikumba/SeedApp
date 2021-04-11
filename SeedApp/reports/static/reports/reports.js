
const data_value = JSON.parse(document.getElementById('data').textContent);
const data = JSON.parse(data_value);
var map;
var summary = {};
var bar_summary=[];
var pie_summary=[];

$(document).ready(function() {
    update_map(data);
    order_summary();
    console.log(summary)
});

//create map function
function update_map(data_list){
    //example cn be found https://leafletjs.com/
    map = L.map('map').setView([39, -99], 4);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    data_list.forEach(function(trial){
    // learn size for popups
    // create a circle for the marker and set colors based on filter
        L.marker([trial.lat, trial.lng])
            .addTo(map)
            .bindPopup(marker_chart(trial));
    });
}

// download chart
// direc svg to canvas to png
// html to png might work
function marker_chart(trial){
    var div = d3.create('div');
    var values = [];
    var names = Array(trial.measures.length).fill('');
    trial.products.forEach(function(product){
            names[product.treatment-1] += product.product;
    });
    trial.measures.forEach(function(measure){
        values.push([names[measure.treatment-1], measure.value]);
        //add kep value to summary
        if(!(names[measure.treatment-1] in summary)){
            summary[names[measure.treatment-1]] = '';
        }
        summary[names[measure.treatment-1]] += (measure.value +',');
    });
    var chart = c3.generate({bindto: div,
            data: {columns: values,
            type:'bar',
            labels:true},
            axis:{
                y:{label:{
                        text: 'Yield b/ac',
                        position: 'outer-middle'}},
                x:{type: 'category',
                   categories:['Treatments']}},
            title:{text:trial.crop+" Trial:"+trial.id},
            size:{// create variables
                width: 250,
                height: 200}});
    return div.node();
}

// get the selected filters
$('#id_countries, #id_crops ,#id_products').change(function(){
    var country = $('#id_countries').val();
    var crop = $('#id_crops').val();
    var product = $('#id_products').val();
    var selected = data;

    if (country != ''){
        selected = selected.filter(s => s.country == country);
    }
    if (crop != ''){
        selected = selected.filter(s => s.crop == crop);
    }
    if(product != ''){
        selected = selected.filter(s => s.products.some(ps => ps.product == product));
    }
    // update markers
    map.off();
    map.remove();
    update_map(selected);
    order_summary();
});

function order_summary(){
    //summarise data
    for(let key in summary){
        var all_values = summary[key].split(',')
        all_values.pop();
        var total=0;
        all_values.forEach(function(i){
            total += parseInt(i);
        });
        console.log(all_values.length, total/all_values.length);
        bar_summary.push([key, total/all_values.length]);
        pie_summary.push([key, all_values.length]);
    }
    bar_chart(bar_summary);
    pie_chart(pie_summary);

    summary = {};
    pie_summary = [];
    bar_summary = [];
}


function bar_chart(list_list){
    var bar = c3.generate({
        bindto: '#barG',
        data: {columns: list_list,
            type:'bar',
            labels:true},
        axis:{y:{
                    label:{
                        text: 'Yield b/ac',
                        position: 'outer-middle'}},
                x:{
                    type: 'category',
                    categories:['Treatments']}},
        title:{text:'Summary Bar Chart'}
    });
}

function pie_chart(list_list){
    var pie = c3.generate({
    bindto: '#pieG',
    data: {columns: list_list,
            type:'pie'},
    title:{text:'Summary Pie Chart'}
    });
}
