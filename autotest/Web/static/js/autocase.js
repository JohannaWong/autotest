

var num = 1;
function addRow(){
           var tb = document.getElementById("mytableid");
   
           console.log()
            var row = tb.insertRow();
             var cell = row.insertCell();
            cell.innerHTML = "<input type='text' name = COMMON___"+num+" value = ''>";
            var cell = row.insertCell();
            cell.innerHTML = "<input type='text' name = VALUE___"+num+" value = ''>";
            var cell = row.insertCell();
            cell.innerHTML = "<input type='text' name = XPATH___"+num+" value = ''>";
            var cell = row.insertCell();
            cell.innerHTML = "<input type='text' name = KEY___"+num+" value = ''>";
            var cell = row.insertCell();
            cell.innerHTML = "<input type='text' name = STEP___"+num+" value = ''>";
            var cell = row.insertCell();
            cell.innerHTML = "<input type='text' name = NO___"+num+" value = ''>";
            var cell = row.insertCell();
            cell.innerHTML = "<div class='delNumId'>"+num+"</div>";
           
            
            num++;
	}
function delRow() {
            var delNumId = $("div.delNumId"); 
            var rowIndex = document.getElementById("delTextId").value;
            for(var i =0; i<delNumId.length;i++){          	
               if(delNumId.eq(i).text()==rowIndex){  
                     delNumId.eq(i).parents("tr").remove();                     
                }           
            }
  
        }
