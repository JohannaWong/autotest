function pageSplit(obj, pno, psize, headNum, footNum,obj1) {
 var itable = document.getElementById(obj);
 var num = itable.rows.length;//表格行数
 var realNum = num - headNum - footNum;//实际数据行数
 var pageSize = psize;//每页显示行数
 
 if(realNum <= pageSize) {
  return;
 }
 
 var totalPage = parseInt((realNum+pageSize-1)/pageSize);//总页数
 var currentPage = pno;//当前页码
 var startRow = (currentPage - 1) * pageSize + 1;//开始显示的行
 var endRow = currentPage * pageSize + 1;//结束显示的行
 endRow = (endRow > num) ? num : endRow;
 
 //前headNum行始终显示
 for (i = 0; i < headNum; i++) {
  var irow = itable.rows[i];
  irow.style.display = "incline";
 }
 for (var i = headNum; i < num - footNum; i++) {
  var irow = itable.rows[i];
  if (i >= startRow && i < endRow) {
   irow.style.display = "";
  } else {
   irow.style.display = "none";
  }
 }
 //后footNum行始终显示
 for (i = num - footNum; i < footNum; i++) {
  var irow = itable.rows[i];
  irow.style.display = "incline";
 }
 
 var tempStr = "共" + currentPage + "/" + totalPage + "页";
 if (currentPage > 1) {
  tempStr += "<a style='cursor:pointer;' onClick=\"pageSplit('" + obj + "'," + (1) + "," + psize + "," + headNum + "," + footNum + ",'" + obj1 + "')\">首页&nbsp</a>";
  tempStr += "<a style='cursor:pointer;' onClick=\"pageSplit('" + obj + "'," + (currentPage - 1) + "," + psize + "," + headNum + "," + footNum + ",'" + obj1 + "')\">&nbsp上一页</a>";
 }
 else {
  tempStr += "首页&nbsp";
  tempStr += "&nbsp上一页";
 }
 if (currentPage < totalPage) {
  tempStr += "<a style='cursor:pointer;' onClick=\"pageSplit('" + obj + "'," + (currentPage + 1) + "," + psize + "," + headNum + "," + footNum + ",'" + obj1 + "')\">&nbsp下一页</a>";
  tempStr += "<a style='cursor:pointer;' onClick=\"pageSplit('" + obj + "'," + (totalPage) + "," + psize + "," + headNum + "," + footNum + ",'" + obj1 + "')\">&nbsp尾页</a>";
 }
 else {
  tempStr += "&nbsp下一页";
  tempStr += "&nbsp尾页";
 }
 
 document.getElementById(obj1).innerHTML = tempStr;
}