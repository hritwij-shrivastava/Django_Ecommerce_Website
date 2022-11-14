 // code for product description page
 $(document).ready(function(){
    var base_url = $('#homeUrl').attr('href');
    var code = $('#color-list-display').attr('class');
    function loadColor(){
      $.ajax({
        url: base_url +  '/boys-m-ajax-color-spliter',
        type: "POST",
        dataType:'json',
        data: {
          code:code,
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          action: 'post'
        },
        success: function(res){
          var _html = '';
          var _html2 = '';
          var color_list = res.color_list;
          var array = color_list.split(',');
          var k = 0;
          if(array!=''){
            for(var i=0; i<Math.ceil(array.length/3); i++){
              for(var j=0; j<3; j++){
                  _html2+='<li style="background-color: '+ array[k] +'; width: 125px;height: 125px;"></li>'
                  k=k+1;
                  if(k>(array.length)-1){
                      break;
                  }
              }
              _html+='<ul>\
                  '+_html2+'\
              </ul>'
              _html2=''
          }
          
          $("#color-list-display").append(_html);
          }
         
        }
      });
  
    }
  
    loadColor();
  });
  
  