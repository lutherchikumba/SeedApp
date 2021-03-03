
      function openNav() {
        document.getElementById("mySidenav").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
      }
      
      function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft= "0";
        document.body.style.backgroundColor = "white";
      }

      function getvalues(){
        var seleted = new Array();
        var chkbox=document.getElementById("tabl");
        var selchk = chkbox.getElementsByTagName("input");
        for(var i = 0; i<selchk.length;i++){
          if(selchk[i].checked){
              seleted.push(selchk[i].value);
          }
        }

        seleted = seleted.join("<br>");
        if(seleted.length > 0){
            document.getElementById("display_values").innerHTML = seleted ;
        }
      };

      $(document).ready(function()
      {
        $('.chkcvalues').click(function()
        {
          var txt = "";
          $('chkcvalues:checked').each(function()
          {
            txt+=$(this).val()+","
          });
          txt = txt.substring(0, txt.length-1);
          $('#txtvalues').val(txt);
        });

      });