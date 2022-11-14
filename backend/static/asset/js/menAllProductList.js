$(document).ready(function(){
  var base_url = $('#homeUrl').attr('href');
  var get_url;
  $(".shop-aside__item ul li:first-child a").addClass("active");
  function loadTable(page){
    var active_ctg = $(".shop-aside__item ul li a.active").attr("id");
    $.ajax({
      url: base_url +  '/m-ajax-pagination',
      type: "POST",
      dataType:'json',
      data: {
        page_no:page,
        active_ctg:active_ctg,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        action: 'post'
      },
      success: function(res){
        var _html = '';
        var json_data = $.parseJSON(res.data_json);
        
        $.each(json_data,function(index,data){
          get_url = base_url +'/static/media/'+ data.fields.product_img;
          product_url = base_url + '/menproduct-description/' + data.fields.product_unique_id

          _html+='<a href="'+product_url+'" class="products-item">\
          <div class="products-item__type">\
              <!-- <span class="products-item__new">new</span> -->\
          </div>\
          <div class="products-item__img">\
              <img src="'+get_url+'"  class="js-img" alt="">\
              <div class="products-item__hover">\
                  <i class="icon-search"></i>\
                  <div class="products-item__hover-options">\
                      <!-- <i class="icon-heart"></i> -->\
                      <!-- <i class="icon-cart"></i> -->\
                  </div>\
              </div>\
          </div>\
          <div class="products-item__info">\
              <span class="products-item__name">'+data.fields.product_name+'</span>\
              <!--<span class="products-item__cost">'+data.fields.product_name+'</span>--> \
          </div>\
      </a>';
      
        });
        $("#wrap-json-html").empty().append(_html);
        $("#check_active").attr("href", page);
        var _html_pagination =''
        data_count = res.total_data;
        $("#last_page").attr("href", data_count);
        for(i=1;i<=data_count;i++){
            _html_pagination+= '<li class="paging-list__item">\
            <a href="#" id="'+i+'" class="paging-list__link">'+i+'</a>\
        </li>';
        $("#paginator_links").empty().append(_html_pagination);

        $("#"+page).parent('li').addClass('active');
        
        
        }
        
      }
    });

  }
  loadTable(1);

  
// pagination code
  $(document).on("click","#pagination a",function(e){
    e.preventDefault();

    var page_id = $(this).attr("id");
    if(page_id == -1){
      current_page=parseInt($("#check_active").attr("href"))
      prev_page=current_page-1
      if(prev_page!=0){
        loadTable(prev_page)
      }       
    }
    if(page_id == -10){
      current_page=parseInt($("#check_active").attr("href"))
      last_page=parseInt($("#last_page").attr("href"))
      next_page=current_page+1
      if(next_page<=last_page){
        loadTable(next_page)
      }       
    }
    else{
      loadTable(page_id)
    }
    

  })

  //category selection code

  $(".shop-aside__item ul li a").on('click',function(e){
    e.preventDefault()
    $(".shop-aside__item ul li a").removeClass("active")
    $(this).addClass("active")
    loadTable(1);

  });

});


 