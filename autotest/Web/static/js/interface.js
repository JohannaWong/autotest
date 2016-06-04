   var tag=1
   var tag1=1 
   var StyleFile = "theme" + document.cookie.charAt(6) + ".css";
   document.writeln('<link rel="stylesheet" type="text/css" href="css/' + StyleFile + '">');
   
   window.onload = incValue;
   function incValue() {
   	   var o = document.getElementById('prog1');
   	   if (o.value == 100){
   	   	   o.value = 0;
   	   } else {
   	   	   o.value+ = 1;
   	   }
   	   window.setTimeout("incValue()",1000);
   }
   
   
   
   function checkpost()
   {
   		if(myform.run_time.value=="" || myform.run_time.value=="0"){alert("请输入正确的运行时间");
    	myform.run_time.focus();
    	return false;
   		}

   		if(myform.threads.value=="" || myform.threads.value=="0"){alert("请输入正确的线程数");
    	myform.threads.focus();
    	return false;
   		}

   		if(myform.processes.value=="" || myform.processes.value=="0"){alert("请输入正确的进程数");
    	myform.processes.focus();
    	return false;
    	}
    	
    	if(myform.script.value=="" || myform.script.value.indexOf(".py")=="-1"){alert("请输入正确的脚本名(例如:test.py)");
    	myform.script.focus();
    	return false;
    	}

    	if(myform.MyFile.value==""){alert("请上传脚本");
    	myform.MyFile.focus();
    	return false;
    	}
    	
 		if(tag==1 && myform.webserver_ip.value==""){alert("请输入服务器地址");
 		myform.webserver_ip.focus();
    	return false;
    	}
 		
 		if(tag==1 && myform.webserver_port.value==""){alert("请输入服务器端口");
 		myform.webserver_port.focus();
    	return false;
    	}
    	
    	if(tag1==1 && myform.host_arg.value==""){alert("请输入数据库IP");
 		myform.host_arg.focus();
    	return false;
    	}
    	
    	if(tag1==1 && myform.port_arg.value==""){alert("请输入数据库端口");
 		myform.port_arg.focus();
    	return false;
    	}
    	
    	if(tag1==1 && myform.user_arg.value==""){alert("请输入数据库用户名");
 		myform.user_arg.focus();
    	return false;
    	}
    	
    	if(tag1==1 && myform.password_arg.value==""){alert("请输入数据库密码");
 		myform.password_arg.focus();
    	return false;
    	}
   }
function msg()
{
	if (confirm("您确认是否提交?"))
	document.zzjs_net.submit()
}