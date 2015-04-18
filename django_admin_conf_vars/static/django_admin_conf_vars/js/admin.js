(function($) {

 $(document).ready(function () {
     $("#result_list .vTextField").attr('disabled', 'disabled');
     $.each($("#result_list .vTextField"), function (i,n) {
         var editable = $(n).closest('tr').find('img').attr('alt');
         if(editable == "True"){
            $(n).attr('disabled', false).css({'padding': '10px 4px'})
         }
     })
 });
})(django.jQuery);