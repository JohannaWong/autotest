$(function(){
    jQuery(".task_num").click(function(){
    		//task_id = $(this).parent().prev().prev().prev().prev().text();
    		//$("#task_id").val(task_id);
    		ietest();
        jQuery("#TB_SRP_DIALOGING").show("normal");
         //jQuery("#TB_SRP_DIALOGING").hide("normal");

    });
    jQuery(".closeButton").click(function(){
         jQuery("#TB_SRP_DIALOGING").hide("normal");
    });
});
		ietest=function(){
			
    var _width=(document.documentElement.clientWidth/2)-(jQuery("#TB_SRP_DIALOGING").width()/2);//窗口宽度 (浏览器宽度/2)-(浮动层宽度/2)
    var _height=(document.documentElement.clientHeight/2)-(jQuery("#TB_SRP_DIALOGING").height()/2);//窗口高度 (浏览器高度/2)-(浮动层高度/2)
    	if (jQuery.browser.version == "6.0")//$.browser.msie ie系列浏览器
    	{
     	document.getElementById('TB_SRP_DIALOGING').style.left=_width;
     	document.getElementById('TB_SRP_DIALOGING').style.top=_height;
    	}
    	else{
        jQuery("#TB_SRP_DIALOGING").css({left:_width,top:_height});
    	}
	}
window.onresize=ietest; //缩放窗体时触发事件


function chk(){
  var obj=document.getElementsByName('task_checkbox');
  var s='';
  for(var i=0; i<obj.length; i++){
    if(obj[i].checked) s+=obj[i].value+'::';
  }
  
  if(s==''){
  	sAlert('请选择至少一个以上测试用例!');
  	return false;
  }
  
  window.open("/ajaxgetreport?report_id="+s);
/*
  jQuery.ajax({
  	type:"GET",
		URL:"ajaxgetreport",
		data:"report_id="+s,
		success:taskorder
	})
*/

}


/*
function taskorder(data)
{
	if (data==0){
		sAlert("请选择三个以下的项目报告进行分析!")
		}
	else{
		sAlert("请选择三个以下的项目报告进行分析!!")
		}		
}
*/

function editcase(data)
{
	
	window.open("/autocase?case_id="+data);	
}

