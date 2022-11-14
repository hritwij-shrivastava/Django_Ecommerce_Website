$(document).ready( function(){
    var base_url = $('#home-link').attr('href');
    function hide_every_row (){
        $('#blog-row').css({"display":"none"});
    }
    function selector(id){
        hide_every_row()
        $(id).css({"display":""});
    
    }
    
    var base_url = $('#home-link').attr('href');
    selector("#blog-row")

    $('.cancel-category-btn').on('click',function(){
        $(this).parents('.card-body').siblings('.card-body').css({"display":""});
        $(this).parents('.card-body').css({"display":"none"});
    });
    $('.adder').on('click',function(){
        $(this).parents('.card-header').siblings('.area-view').css({"display":""});
        $(this).parents('.card-header').siblings('.table-view').css({"display":"none"});
    });
    $('.title-header').on('click',function(){
        $(this).parents('.card-header').siblings('.area-view').css({"display":"none"});
        $(this).parents('.card-header').siblings('.table-view').css({"display":""});
    });
    
    $('#blog-selector').on('click',function(){
        selector("#blog-row")
    });

    $('#submit-blog-edit-form').submit(function(e){
        e.preventDefault();
        $('.loader-animate').removeClass('loader-hide');

        id = $("#blog-edit-input").val()
        if(id!=''){
            $.ajax({
                url: "/my-adminpage/edit-blog-request",
                type: 'POST',
                data: {
                    id: id,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
                },
        
                success: function(json){
                    $('.loader-animate').addClass('loader-hide');
                    if(json.status == 1){
                        location.replace( base_url +  "/my-adminpage/edit-blog/"+id)
                    }
                    else{
                        alert(json.title)
                    }
                    
                }
        
            });
        }
        
    });
});