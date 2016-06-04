var context = this;
   jQuery("input[@type='radio'] + label", this)
     .each( function(){
     if (jQuery(this).prev().attr('name') == "radio2")
           jQuery(this).addClass("checked_1");
       })
     .hover(
       function() { $(this).addClass("over"); },
       function() { $(this).removeClass("over"); }
     )
     .click( function() {
       jQuery("input[@type='radio'] + label", context)
         .each( function() {
           jQuery(this)
             .removeClass()
             .prev()[0].checked = false;
         });
        
         if(jQuery(this).prev().attr('name') == "radio1") {
           jQuery(this).addClass("checked").prev()[0].checked = true;
         }
         else
         jQuery(this).addClass("checked_1");
       })
     .prev().hide();
}
