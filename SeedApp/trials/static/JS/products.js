
      // function openNav() {
      //   document.getElementById("mySidenav").style.width = "250px";
      //   document.getElementById("main").style.marginLeft = "250px";
      //   document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
      // }
      
      // function closeNav() {
      //   document.getElementById("mySidenav").style.width = "0";
      //   document.getElementById("main").style.marginLeft= "0";
      //   document.body.style.backgroundColor = "white";
      // }

      // function getvalues(){
      //   var seleted = new Array();
      //   var chkbox=document.getElementById("tabl");
      //   var selchk = chkbox.getElementsByTagName("input");
      //   for(var i = 0; i<selchk.length;i++){
      //     if(selchk[i].checked){
      //         seleted.push(selchk[i].value);
      //     }
      //   }

      //   seleted = seleted.join("<br>");
      //   if(seleted.length > 0){
      //       document.getElementById("display_values").innerHTML = seleted ;
      //   }
      // };

      // $(document).ready(function()
      // {
      //   $('.chkcvalues').click(function()
      //   {
      //     var txt = "";
      //     $('chkcvalues:checked').each(function()
      //     {
      //       txt+=$(this).val()+","
      //     });
      //     txt = txt.substring(0, txt.length-1);
      //     $('#txtvalues').val(txt);
      //   });

      // });


var t1copy = $( ".C-1" ).clone( true );
var p1copy = $( ".P-1" ).clone( true );

//adding treatments and products
$("#addTreatment").click(function(){
    var product = t1copy.clone(true);
    addT(product, 't');
});
$(document).on('click', '.addP', function(e){
    var id = this.id.replace(/[^0-9]/g,'');
    var product = p1copy.clone(true);
    addT(product,'p', id);
});


//subtracting treatments and products
$("#subTreatment").click(function(){
    var last = $('#NumberOfTreatments').val();
    var total = $('#id_form-TOTAL_FORMS').val();
    var products = $(".C-"+last).children('div').length;
    if(last > '1'){
        $('.C-'+last).remove();
        total = Number(total) - Number(products)
        last--;
        $('#NumberOfTreatments').val(last);
        $('#id_form-TOTAL_FORMS').val(total);
        var forms = $('*[class*="P-"]');
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).attr('class', 'P-'+(i+1))
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, 'form', i);
            });
            $(forms.get(i)).find('label').each(function() {
                updateElementIndex(this, 'form', i);
            });
        }
    }
});
$(document).on('click', '.subP', function(){
    var id = this.id.replace(/[^0-9]/g,'');
    subP(id);
});

//sub helper
function subP(id) {
    var total = $(".C-"+id).children('div').length;
    if (total > 1){
        $(".C-"+id).children().last().remove();
        var total = $('#id_form-TOTAL_FORMS').val();
        total--;
        $('#id_form-TOTAL_FORMS').val(total);
        var forms = $('*[class*="P-"]');
        for (var i=0, formCount=total; i<formCount; i++) {
            $(forms.get(i)).attr('class', 'P-'+(i+1))
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, 'form', i);
            });
            $(forms.get(i)).find('label').each(function() {
                updateElementIndex(this, 'form', i);
            });
        }
    }
}
function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}


//add helper
function addT(treatment, t, id) {
    var newElement = treatment
    var numTreatments = $('#NumberOfTreatments').val();
    var total = $('#id_form-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name').replace('-' + 0 + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id});
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + 0 + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_form-TOTAL_FORMS').val(total);
    if(t === "t"){
        numTreatments++;
        $('#NumberOfTreatments').val(numTreatments);
        $(newElement).insertBefore('#addTreatment')
        $(newElement).attr('class', 'C-'+numTreatments);
        newElement.find('#addP-1').each(function() {
            $(this).attr('id','addP-'+numTreatments);
        });
        newElement.find('#subP-1').each(function() {
            $(this).attr('id','subP-'+numTreatments);
        });
        newElement.find('h3').each(function() {
            $(this).replaceWith('<h3>T-'+numTreatments+'</h3>');
        });
        newElement.find('.P-1').each(function() {
            $(this).attr('class', 'P-'+total)
        });
        $('#id_form-' + (total-1) +'-treatment').val(numTreatments);
    }
    else{
        $(newElement).attr('class', 'P-'+total);
        $(".C-"+id).append(newElement);
        $('#id_form-' + (total-1) +'-treatment').val(id);
    }
}