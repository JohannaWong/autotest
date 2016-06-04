


//调试-开始
function viewinterfacedetail(caseinfo,requesturl,username,password,textareaparam,protocal_id,request_type,Content_type)
{	
	
	jQuery.ajax({ 
		type:"GET", 
		url:"ajaxinterfacedetail", 
		data:"caseinfo="+caseinfo+"&requesturl="+requesturl+"&username="+username+"&password="+password+"&textareaparam="+textareaparam+"&protocal_id="+protocal_id+"&request_type="+request_type+"&Content_type="+Content_type,
		success:ajaxinterfacedetail_Response 
		}); 
		
}

function ajaxinterfacedetail_Response(ajaxinterfacedetail)
{	
	
		
		var $testinterface_table=jQuery("#testinterface_table");
		$testinterface_table.html("");
		http_code = ajaxinterfacedetail.split('Http:')[1].split("'")[0];
		$testinterface_table.append("<tr><td>"+"HttpResponse"+"</td><td>"+http_code+"</td></tr>")
		$testinterface_table.append("<tr><td>"+"result"+"</td><td>"+ajaxinterfacedetail+"</td></tr>")
		jQuery("#testinterface").show("normal");
		$testinterface_table.show("normal");

	
}

function closeDiv(){ 
document.getElementById('testinterface').style.display='none'; 
document.getElementById('testinterface_table').style.display='none'; 
} 

function closeDivshowcase(){ 
document.getElementById('showcase').style.display='none'; 
document.getElementById('showcase_table').style.display='none'; 
} 

//调试-结束

function ajaxshowcasedetail(case_id)
{	
	jQuery.ajax({ 
		type:"GET", 
		url:"showcasedetail", 
		data:"case_id="+case_id,
		success:showcasedetail_Response 
		}); 
		
}

function showcasedetail_Response(ajaxshowcasedetail)
{		
		var $showcase_table=jQuery("#showcase_table");
		result = eval('(' + ajaxshowcasedetail + ')');
		$showcase_table.html("");
		var size = result.length;
		for(i=0;i< size;i++)
			{
				jQuery("#showcase_table").append("<tr><td>"+result[i].label+"</td><td>"+result[i].value+"</td></tr>")
			}
		
		jQuery("#showcase").show("normal");
		$showcase_table.show("normal");
	
}
