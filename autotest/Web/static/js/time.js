var CID = "endtime";
if(window.CID != null)
{
    var iTime = document.getElementById(CID).innerText;
    var Account;
    RemainTime();
}
function RemainTime()
{
    var iDay,iHour,iMinute,iSecond;
    var sDay="",sHour="",sMinute="",sSecond="",sTime="";
    if (iTime >= 0)
    {
        iDay = parseInt(iTime/24/3600);
        if (iDay > 0)
        {
            sDay = iDay + "��";
        }
        iHour = parseInt((iTime/3600)%24);
        if (iHour > 0){
            sHour = iHour + "Сʱ";
        }
        iMinute = parseInt((iTime/60)%60);
        if (iMinute > 0){
            sMinute = iMinute + "����";
        }
        iSecond = parseInt(iTime%60);
        if (iSecond >= 0){
            sSecond = iSecond + "��";
        }
        if ((sDay=="")&&(sHour=="")){
            sTime="<span style='color:darkorange'>" + sMinute+sSecond + "</font>";
        }
        else
        {
            sTime=sDay+sHour+sMinute+sSecond;
        }
        if(iTime==0){
            clearTimeout(Account);
              sTime="<span style='color:green'>ʱ�䵽�ˣ�</span>";
        }
        else
        {
            Account = setTimeout("RemainTime()",1000);
        }
        iTime=iTime-1;
    }
    else
    {
            sTime="<span style='color:red'>����ʱ������</span>";
    }
    document.getElementById(CID).innerHTML = sTime;
}