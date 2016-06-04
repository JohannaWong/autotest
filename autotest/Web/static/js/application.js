
function sAlert(txt)
{
    var eSrc=(document.all)?window.event.srcElement:arguments[1];
    var shield = document.createElement("DIV");
    shield.id = "shield";
    shield.style.position = "absolute";
    shield.style.left = "-1px";
    shield.style.top = "-15px";
    shield.style.width = "100%";
    shield.style.height = "1100px"//document.body.scrollHeight+"px";
    shield.style.background = "#2E2E2E";
    shield.style.textAlign = "center";
    shield.style.zIndex = "770";
    shield.style.filter = "alpha(opacity=0)";
    shield.style.opacity = 0;
    var alertFram = document.createElement("DIV");
    alertFram.id="alertFram";
    alertFram.style.position = "absolute";
    alertFram.style.left = "50%";
    alertFram.style.top = "50%";
    alertFram.style.marginLeft = "-225px" ;
    alertFram.style.marginTop = -75+document.documentElement.scrollTop+"px";
    alertFram.style.width = "400px";
    alertFram.style.height = "150px";
    alertFram.style.background = "#ccc";
    alertFram.style.textAlign = "center";
    alertFram.style.lineHeight = "100px";
    alertFram.style.zIndex = "777";
    strHtml = "<ul style=\"list-style:none;margin:0px;padding:0px;width:100%\">\n";
    strHtml += " <li style=\"background:#930000;font-family:Microsoft YaHei;text-align:left;padding-left:20px;font-size:14px;font-weight:bold;height:25px;line-height:25px;border:1px solid #F9CADE;\">测试平台提示您:</li>\n";
    strHtml += "    <li style=\"background:#fff;font-family: Microsoft YaHei;text-align:center;font-size:12px;height:100px;line-height:100px;border-left:1px solid #FFFFFF;border-right:1px solid #F9CADE;\">"+txt+"</li>\n";
    strHtml += "    <li style=\"background:#FDEEF4;font-family:Microsoft YaHei;text-align:center;font-weight:bold;height:25px;line-height:25px; border:1px solid #FFFFFF;\"><input type=\"button\" style=\"font-family:Microsoft YaHei;\" value=\"确 定\" id=\"do_OK\" onclick=\"doOk();\"/></li>\n";
    strHtml += "</ul>\n";
    alertFram.innerHTML = strHtml;
    document.body.appendChild(alertFram);
    document.body.appendChild(shield);
    this.setOpacity = function(obj,opacity)
    {
        if(opacity>=1)opacity=opacity/100;
        try
        {
            obj.style.opacity=opacity;
        }
        catch(e)
        {}
        try
        {
            if(obj.filters.length>0&&obj.filters("alpha"))
            {
                obj.filters("alpha").opacity=opacity*100;
            }
            else
            {
                obj.style.filter="alpha(opacity=\""+(opacity*100)+"\")";
            }
        }
        catch(e)
        {}
    }
    var c = 0;
    this.doAlpha = function()
    {
        if (++c > 20)
        {
            clearInterval(ad);
            return 0;
        }
        setOpacity(shield,c);
    }
    var ad = setInterval("doAlpha()",1);
    this.doOk = function()
    {
        document.body.removeChild(alertFram);
        document.body.removeChild(shield);
        eSrc.focus();
        document.body.onselectstart = function(){return true;}
        document.body.oncontextmenu = function(){return true;}
        
        document.getElementsByName("do_OK").focus();
    	eSrc.blur();
    	document.body.onselectstart = function(){return false;}
    	document.body.oncontextmenu = function(){return false;}
    }

}
