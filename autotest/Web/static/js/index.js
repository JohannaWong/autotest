$(function(){


    jQuery(".closeButton").click(function(){
         //jQuery("#TB_SRP_DIALOG").hide("normal");
         //jQuery("#test").hide("normal");
         jQuery(".search-popup-window").hide("normal");
    });
    
    jQuery(".test1").click(function(){
			case_id = jQuery(this).parent().prev().prev().prev().prev().text();
    	jQuery("#case_id").val(case_id);
    	ietest_new("test");
      jQuery("#test").show("normal");
    });
});

jQuery(document).ready(function(){

	pageSplit('pTable',1,5,1,1,'pSpan');
	jQuery("#plan_submit_time").datepicker(); 
	jQuery("#submit_test_time").datepicker(); 
	jQuery("#release_time").datepicker(); 

});



//查看项目详情-开始
function viewprojectdetail(project_id)
{
	jQuery.ajax({ 
		type:"GET", 
		url:"ajaxprojectdetail", 
		data:"project_id="+project_id, 
		success:ajaxprojectdetail_Response 
		}); 
}

function ajaxprojectdetail_Response(data)
{
	result = eval('(' + data + ')');
	jQuery("#project_detail_table").html("");
	var size = result.length;
	for(i=0;i<size;i++)
	{
		jQuery("#project_detail_table").append("<tr><td>"+result[i].label+"</td><td>"+result[i].value+"</td></tr>")
	}
	ietest_new("project_detail");
    jQuery("#project_detail").show("normal");
}


//查看项目详情-结束


//查看测试结果-开始
function downloadreport(project_id)
{	
	jQuery.ajax({ 
		type:"GET", 
		url:"ajaxprojectinfo", 
		data:"project_id="+project_id, 
		success:ajaxprojectdetail_Response 
		}); 
}

function ajaxprojectdetail_Response(data)
{
	result = eval('(' + data + ')');
	jQuery("#projectinfo_detail_table").html("");
	var size = result.length;
	for(i=0;i< size;i++)
	{
		jQuery("#projectinfo_detail_table").append("<tr><td>"+result[i].label+"</td><td>"+result[i].value+"</td></tr>")
	}
	ietest_new("projectinfo_detail");
    jQuery("#projectinfo_detail").show("normal");
}
//查看测试结果-结束


//项目状态展示逻辑-开始
function uploaddata(project_id_hidden)
{
    jQuery("#project_id_hidden").val(project_id_hidden);
    ietest_new("report");
    jQuery("#report").show("normal");
}
//项目状态展示逻辑-结束



//项目状态更新-开始
function projectstatus(status_num,project_id)
{
	var r=confirm("确认要执行完成操作吗？");
    if (r==false)
    {
    return;
    }
	
	jQuery.ajax({
		type:"GET",
		url:"ajaxprojectstatus",
		data:"status_num="+status_num+"&project_id="+project_id,
		success:function(){
            window.location.reload(); //刷新当前父页面
            
        }
		});
}
//项目状态更新-结束

//项目提交时，进行数据正确性验证
function checkpost()
{
alert(111);
	if(project_info.project_name.value==""){sAlert("请输入项目名称");
	project_info.project_name.focus();
	return false;
		}
		
		if(project_info.project_commiter.value==""){sAlert("请输入提交人~");
	project_info.project_commiter.focus();
	return false;
		}

		if(project_info.plan_submit_time.value==""){sAlert("请选择项目计划提交时间~");
	project_info.plan_submit_time.focus();
	return false;
		}

		if(project_info.submit_test_time.value==""){sAlert("请选择项目提交时间~");
	project_info.submit_test_time.focus();
	return false;
	}

	if(project_info.release_time.value==""){sAlert("请选择实际上线时间~");
	project_info.release_time.focus();
	return false;
	}
	
	if(project_info.release_time.value < project_info.submit_test_time.value ||project_info.release_time.value < project_info.plan_submit_time.value){sAlert("时间选择错误,请重新选择~")
	project_info.release_time.focus();
	return false;
	}
	
	if(project_info.test_request_desc.value==""){sAlert("请选择测试需求说明");
	project_info.test_request_desc.focus();
	return false;
	}
}

ietest_new=function(div_id){
	
    var _width=(document.documentElement.clientWidth/2)-(jQuery("#"+div_id).width()/2);//窗口宽度 (浏览器宽度/2)-(浮动层宽度/2)
    var _height=(document.documentElement.clientHeight/2)-(jQuery("#"+div_id).height()/2);//窗口高度 (浏览器高度/2)-(浮动层高度/2)
    	if (jQuery.browser.version == "6.0")//$.browser.msie ie系列浏览器
    	{
     	document.getElementById(div_id).style.left=_width;
     	document.getElementById(div_id).style.top=_height;
    	}
    	else{
        jQuery("#"+div_id).css({left:_width,top:_height});
    	}
	}
