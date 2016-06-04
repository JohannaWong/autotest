function createhtmlreport()
	{
		//TODO: JS 验证
		//alert(jQuery("#creat_report_project").val());
		//alert(jQuery("#creat_report_task").val());
		project_id = jQuery("#creat_report_project").val();
		task_optbest = jQuery("#creat_report_task_bestopt").val();
		creat_report_task="";
		jQuery(jQuery("input[name='creat_report_task'][checked]")).each(function(){creat_report_task+=this.value +',';});
		creat_report_task = creat_report_task.substring(0,creat_report_task.length-1);
		url = "/htmlreport?project_id="+project_id+"&task_list="+creat_report_task+"&task_id_opt="+task_optbest;
		alert(url);
		window.open (url); 
	}