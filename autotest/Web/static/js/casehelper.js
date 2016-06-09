$(function(){
	//SLOT改变产品线id,项目ID改变
	jQuery("#productline_id").change(refresh_projects);
	//SLOT改变caseid,def改变
	jQuery("#case_id").change(refresh_case);

	//刷新case
	jQuery("#check_case").click(checkcase);
	
	jQuery("#select_script_complete").click(function(){
		//利用下拉列表选择script
		jQuery("#script_id").val(jQuery("#select_script_dropdown_list").val());
		script_name = jQuery("#select_script_dropdown_list option:selected").text().trim();
		jQuery("#uploader").val(script_name);
        jQuery("#TB_SRP_DIALOG").hide("normal");
		
    });
	
    jQuery("#select_script").click(
		
		function()
			{
			if(jQuery.trim(jQuery("#project_id").val()) == '')
			{
				sAlert("请选择项目!  (注:如无对应项目，在项目管理增加)");
				return false;
			}
			jQuery.ajax({ 
			type:"GET", 
			url:"ajaxgetautopyscript", 
			data:"project_id="+jQuery("#project_id").val(), 
			beforeSend:select_script_loading,
			success:select_script_Response 
			}) 
			}
	);
    

    jQuery(".closeButton").click(function(){
         //jQuery("#TB_SRP_DIALOG").hide("normal");
         //jQuery("#test").hide("normal");
         jQuery(".search-popup-window").hide("normal");
    });
    
    jQuery("input[name='button_create_task']").click(function(){
		case_id = jQuery(this).parent().prev().prev().prev().prev().text();
    	jQuery("#create_task_div_case_id").val(case_id);
    	ietest_new("test");
       jQuery("#test").show("normal");
    });
    
});


$(document).ready(function(){
	//SLOT刷新project list select
	refresh_projects();
	//SLOT刷新case
	refresh_case();
	//doProcess(jQuery("#case_type").val());
	check_case();
	
	//生成脚本按钮点击操作
    jQuery("#create_script").click(function(){
    	if(jQuery.trim(jQuery("#project_id").val()) == '')
			{
			sAlert("请选择项目!  (注:如无对应项目，在项目管理增加)");
			return false;
			}
    	ietest_new("create_autopy_script_dialog");
    	jQuery("#create_autopy_script_dialog").show("normal");
    });
    
    //生成脚本面板中，确认完成操作
    jQuery("#create_autopy_script_complete").click(function(){
    	//首先检测输入项目的有效性
    	if(check_createscript()==false){
    		return false
    	}
    	
		
    	//ajax 
    	jQuery.ajax({
			type:"POST", 
			url:"ajaxcreateautopyscript", 
			//data:"project_id="+jQuery("#project_id").val(), 
			data:{
				project_id:jQuery("#project_id").val(),
				create_autopy_script_name: jQuery("#create_autopy_script_name").val(), 
				create_autopy_script_url: jQuery("#create_autopy_script_url").val(),
				create_autopy_script_file: jQuery("#create_autopy_script_file").val(),
				create_autopy_script_param: jQuery("#create_autopy_script_param").val(),
				//requesthost:jQuery('input:radio[name="requesthost"]:checked').val(),
				//create_autopy_script_host:jQuery("#create_autopy_script_host").val(),
				requestmothed:jQuery('input:radio[name="requestmothed"]:checked').val(),
				returnstr:jQuery('input:radio[name="returnstr"]:checked').val(),
				returncontent:jQuery("#returncontent").val(),
				returnrecode:jQuery("#returnrecode").val()
					},
			success:create_script_Response 
			}) 
    	
    });
    jQuery(":input[name='task_type']").change(function(){
    	if(jQuery("input:radio[name='task_type']:checked").val() == '1')
    	{
    		jQuery("#excute_timing_div").show();
    	}
    	else
    	{
    		jQuery("#excute_timing_div").hide();
    	}

    })
    
    //jQuery('#selectedDateTime').datetimepicker();
    
    
});

//对于创建任务的参数进行数据验证
function checkcreatetask()
{
	if(jQuery("input:radio[name='task_type']:checked").val() == '1' 
		&& jQuery.trim(jQuery("input[name='excute_timing']").val()) == '')
	{
		sAlert("请输入定时的时间");
		return false;
	}
}

//参数化创建Autopy 脚本，ajax提交前，进行js数据正确性验证
function check_createscript()
{
	if(jQuery("#create_autopy_script_name").val() == '')
	{
		sAlert("请输入自定义脚本名称");
		jQuery("#create_autopy_script_name").focus();
		return false;
	}
	if(jQuery("#create_autopy_script_file").val() == '')
	{
		sAlert("请输入自定义脚本文件名");
		jQuery("#create_autopy_script_file").focus();
		return false;
	}
	if(jQuery("#create_autopy_script_url").val() == '')
	{
		sAlert("请输入URL");
		jQuery("#create_autopy_script_url").focus();
		return false;
	}
	if(tag2==1 && jQuery("#create_autopy_script_param").val() == '')
	{
		sAlert("请输入请求的参数");
		jQuery("#create_autopy_script_param").focus();
		return false;
	}
	
	if(tag3==1 && jQuery("#returncontent").val() == '')
	{
		sAlert("请输入返回信息中校验的关键字");
		jQuery("#returncontent").focus();
		return false;
	}
	
	if(tag3==1 && jQuery("#returnrecode").val() == '')
	{
		sAlert("请输入校验的HTTP返回码");
		jQuery("#returncontent").focus();
		return false;
	}

}

function create_script_Response(data){
	result = eval('(' + data + ')');
	jQuery("#script_id").val(result.script_id);
	jQuery("#uploader").val(result.name + "-" + result.script_orignal_name);
  jQuery(".search-popup-window").hide("normal");
}

function check_case(){
            jQuery.ajax({ 
              type:"GET", 
              url:"ajax_check_case", 
              async: false,
            // success:alert("添加成功"),
              }) 
            window.location.reload();
       } 

//SLOTSLOT传参数传参数，选择productline下拉的时候传参数吧
function refresh_projects(){
	jQuery("#def_id option").remove();
	jQuery.ajax({ 
		type:"GET", 
		url:"ajaxgetprojects", 
		async: false,
		data:"productline_id="+jQuery("#productline_id").val(), 
		//beforeSend:select_script_loading,
		success:refresh_projects_list
		}) 
	refresh_case();
		
}

//SlotSLOTSLOTslot响应产品线的变化，刷新project list
function refresh_projects_list(data)
{
	result = eval('(' + data + ')');
	jQuery("#case_id").html("");
	var size = result.length;
	for(i=0;i< size;i++)
	{
		jQuery("#case_id").append("<option value="+result[i].caseid+">"+result[i].casename+"</option>")
	}
	//jQuery("#case_id").html("<option value="+result[0].case_id+">"+>result[0].case_name+"</option>")
}

//SLOTSLOT传参数传参数，选择case下拉的时候传参数吧
function refresh_case(){
	jQuery.ajax({ 
		type:"GET", 
		url:"ajax_get_case", 
		async: false,
		data:"case_id="+jQuery("#case_id").val(), 
		//beforeSend:select_script_loading,
		success:refresh_case_list 
		}) 
		
}

//SlotSLOTSLOTslot响应case的变化，刷新def
function refresh_case_list(data)
{
	result = eval('(' + data + ')');
	jQuery("#def_id").html("<option value=1>all</option>");
	var size = result.length;
	for(i=0;i< size;i++)
	{
		jQuery("#def_id").append("<option value="+result[i].defid+">"+result[i].defname+"</option>")
	}
}



//查看case详情相关- 开始
function viewcasedetail(case_id)
{
	jQuery.ajax({ 
		type:"GET", 
		url:"ajaxcasedetail", 
		data:"case_id="+case_id, 
		success:ajaxcasedetail_Response 
		}); 
}
function ajaxcasedetail_Response(data)
{
	result = eval('(' + data + ')');
	jQuery("#case_detail_table").html("");
	var size = result.length;
	for(i=0;i< size;i++)
	{
		jQuery("#case_detail_table").append("<tr><td>"+result[i].label+"</td><td>"+result[i].value+"</td></tr>")
		//jQuery("#case_detail_table").append("<option value="+result[i].id+">"+result[i].name+"-"+result[i].script_orignal_name+"</option>")
	}
	ietest_new("case_detail");
    jQuery("#case_detail").show("normal");
}

//查看case详情相关- 结束


//查看效率测试详情相关 - 开始
function vieweffcasedetail(case_id)
{
	jQuery.ajax({ 
		type:"GET", 
		url:"ajaxeffcasedetail", 
		data:"case_id="+case_id, 
		success:ajaxeffcasedetail_Response
		}); 
}

function ajaxeffcasedetail_Response(data)
{
	result = eval('(' + data + ')');
	jQuery("#case_detail_table").html("");
	var size = result.length;
	for(i=0;i< size;i++)
	{
		jQuery("#case_detail_table").append("<tr><td width='100px'>"+result[i].label+"</td><td width='100px'>"+result[i].value+"秒</td></tr>")
	}
	ietest_new("case_detail");
    jQuery("#case_detail").show("normal");
}
//查看效率测试详情相关 - 结束


function select_script_loading()
{
	
}

function select_script_Response(data)
{
	result = eval('(' + data + ')');
	jQuery("#select_script_dropdown_list").html("");
	var size = result.length;
	for(i=0;i< size;i++)
	{
		jQuery("#select_script_dropdown_list").append("<option value="+result[i].id+">"+result[i].name+"-"+result[i].script_orignal_name+"</option>")
	}
	ietest();
    jQuery("#TB_SRP_DIALOG").show("normal");
}



//ajax 上传脚本
function ajaxFileUpload()
{
		
			if(jQuery("#custom_script_name").val()==""){sAlert("请选择自定义脚本名");
			jQuery("#custom_script_name").focus();
    		return false;
   		}
		
			if(jQuery("#autopy_script_file").val()==""){sAlert("请选择上传脚本");
			jQuery("#autopy_script_file").focus();
    		return false;
   		}
		/*
			prepareing ajax file upload
			url: the url of script file handling the uploaded files
                        fileElementId: the file type of input element id and it will be the index of  $_FILES Array()
			dataType: it support json, xml
			secureuri:use secure protocol
			success: call back function when the ajax complete
			error: callback function when the ajax failed
			
                */
		jQuery.ajaxFileUpload
		(
			{
				url:'ajaxuploadautopyscript', 
				secureuri:false,
				fileElementId:'autopy_script_file',
				dataType: 'json',
				data:{project_id:jQuery("#project_id").val(), custom_script_name:jQuery("#custom_script_name").val()},
				//data:[{'name':"project_id","value":jQuery("#project_id").val()},{"name":"custom_script_name","value":jQuery("#custom_script_name").val()}],
				success: function (data, status)
				{
					//设置隐藏的script_id
					messaga_return = data.msg;
					result = eval('(' + messaga_return + ')');
					jQuery("#script_id").val(result.script_id);
					script_name = result.name+"-"+result.script_orignal_name;
					jQuery("#uploader").val(script_name);
					jQuery("#TB_SRP_DIALOG").hide("normal");
				},
				error: function (data, status, e)
				{
					alert(e);
				}
			}
		)
		
		return false;
}

//创建AUTOpy 测试用例之前进行数据正确性的验证
function checkpost()
{
	if(myform.case_name.value=="" || myform.case_name.value=="0"){sAlert("请输入用例名称");
 		myform.case_name.focus();
 	return false;
		}
		
	if(myform.run_time.value=="" || myform.run_time.value=="0"){sAlert("请输入运行时间(单位:秒)");
 		myform.run_time.focus();
 	return false;
		}

	if(myform.threads.value=="" || myform.threads.value=="0"){sAlert("请输入正确的线程数(例如:30)");
 		myform.threads.focus();
 	return false;
		}

	if(myform.proceses.value=="" || myform.proceses.value=="0" || parseInt(myform.proceses.value) > parseInt(myform.threads.value)){sAlert("进程数不能大于线程数！");
 		myform.proceses.focus();
 	return false;
 	}

 	if(myform.script_orignal_name.value=="" || myform.script_orignal_name.value.indexOf(".py")=="-1" || myform.script_orignal_name.value.indexOf(document.getElementById("select_script_dropdown_list"))>=0 ){sAlert("脚本名输入错误！请选择生成脚本方式");
 		myform.script_orignal_name.focus();
 	return false;
 	}
 	
	if(tag==1 && myform.webserver_ip.value==""){sAlert("请输入服务器地址");
		myform.webserver_ip.focus();
 	return false;
 	}
		
	if(tag==1 && myform.webserver_port.value==""){sAlert("请输入服务器端口");
		myform.webserver_port.focus();
 	return false;
 	}
 	
 	if(tag1==1 && myform.host_arg.value==""){sAlert("请输入数据库IP");
		myform.host_arg.focus();
 	return false;
 	}
 	
 	if(tag1==1 && myform.port_arg.value==""){sAlert("请输入数据库端口");
		myform.port_arg.focus();
 	return false;
 	}
 	
 	if(tag1==1 && myform.user_arg.value==""){sAlert("请输入数据库用户名");
		myform.user_arg.focus();
 	return false;
 	}
 	
 	if(tag1==1 && myform.password_arg.value==""){sAlert("请输入数据库密码");
		myform.password_arg.focus();
 	return false;
 	}
 	
	if(tag4==1 && myform.host_cname.value==""){sAlert("请输入要绑定Host的域名");
 		myform.host_cname.focus();
 	return false;
	}
	
	if(tag4==1 && myform.host_ip.value==""){sAlert("请输入要绑定HOST的ip地址");
 		myform.host_ip.focus();
 	return false;
	}
	
}




	ietest=function(){
			
    var _width=(document.documentElement.clientWidth/2)-(jQuery("#TB_SRP_DIALOG").width()/2);//窗口宽度 (浏览器宽度/2)-(浮动层宽度/2)
    var _height=(document.documentElement.clientHeight/2)-(jQuery("#TB_SRP_DIALOG").height()/2);//窗口高度 (浏览器高度/2)-(浮动层高度/2)
    	if (jQuery.browser.version == "6.0")//$.browser.msie ie系列浏览器
    	{
     		document.getElementById('TB_SRP_DIALOG').style.left=_width;
     		document.getElementById('TB_SRP_DIALOG').style.top=_height;
    	}
    	else{
        jQuery("#TB_SRP_DIALOG").css({left:_width,top:_height});
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
window.onresize=ietest; //缩放窗体时触发事件