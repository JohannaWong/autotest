$(document).ready(function(){
	var newSelect = jQuery("#aa");
	newSelect.click(function(e){
		if(this.className == "open"){
			closeSelect(this);
		}else{
			this.className = "open";
			jQuery(this.nextSibling).slideDown("fast");
		}
		e.stopPropagation();
	});
	
	function closeSelect(obj){
		jQuery(obj.nextSibling).slideUp("fast",function(){
			obj.className = "";
		});
	}
	jQuery(document).bind("click", function() {
	  	closeSelect(newSelect[0]);
	});

	newSelect.next().click(function(e){
		var src = e.target;
		if(src.tagName == "A"){
			var PObj = src.parentNode;
			PObj.previousSibling.innerHTML = src.innerHTML;
			/*var aList = PObj.getElementsByTagName("a");
			for(var i=0;i<aList.length;i++){
				aList[i].className = "";
			}*/
			jQuery(src).siblings().removeClass();
			src.className = "current";
			PObj.nextSibling.value = src.getAttribute("value");
		}
	});
});