
//创建AUTOpy 测试用例之前进行数据正确性的验证
function checkpost(){
	var textbox=document.getElementsByName('flag');
	//var flag = 0;//没有选中
	var i;
	 for(i=0;i<textbox.length;i++){
            //alert(textbox[i].checked)
	     if(textbox[i].checked){
	    	 flag = 1;//有选中
	    	 break;
	     }else{
	    	 flag = 0;
	     }
     }
	 if(flag==0){//始终没有选中
		 alert("请选择一条case");
	 }
	 
	 var obj = document.getElementById("button1"); 
	 
	 obj.setAttribute("readOnly",true); 
	 
	 obj.style.backgroundColor="#d2d2d2"; 
	
	 obj.value = "程序执行中... ...";
}
