function hide_every_row (){
    $('#slider-row').css({"display":"none"});
    $('#header-row').css({"display":"none"});
    $('#product-row').css({"display":"none"});
    $('#upslider-row').css({"display":"none"});
    $('#logo-row').css({"display":"none"});
    $('#ad-row').css({"display":"none"});
    $('#insta-row').css({"display":"none"});
}
function selector(id){
    hide_every_row()
    $(id).css({"display":""});

}

$(document).ready(function(){
    $('.selector-shadow').hover(function(){
        $(this).removeClass('shadow');
        },function(){
            $(this).addClass('shadow'); 
        }
    );

    selector("#slider-row")
});

$('.cancel-category-btn').on('click',function(){
    $(this).parents('.card-body').siblings('.card-body').css({"display":""});
    $(this).parents('.card-body').css({"display":"none"});
});
$('.adder').on('click',function(){
    $(this).parents('.card-header').siblings('.area-view').css({"display":""});
    $(this).parents('.card-header').siblings('.table-view').css({"display":"none"});
    $('#category-text-input').val('');
    $('#brand-text-input').val('');
    $('#tags-text-input').val('');
});
$('.title-header').on('click',function(){
    $(this).parents('.card-header').siblings('.area-view').css({"display":"none"});
    $(this).parents('.card-header').siblings('.table-view').css({"display":""});
});

$('#slider-selector').on('click',function(){
    selector("#slider-row")
});

$('#header-selector').on('click',function(){
    selector("#header-row")
});

$('#product-selector').on('click',function(){
    selector("#product-row")
});

$('#upslider-selector').on('click',function(){
    selector("#upslider-row")
});

$('#logo-selector').on('click',function(){
    selector("#logo-row")
});

$('#ad-selector').on('click',function(){
    selector("#ad-row")
});

$('#insta-selector').on('click',function(){
    selector("#insta-row")
});


$('#submit-slider-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    formdata = new FormData();
    k= parseInt($('#slider-img-input').get(0).files.length)
    for (let i = 0; i < k; i++) {
        slider_img_input= ($('#slider-img-input'))[0].files[i];
        formdata.append("slider_img_input", slider_img_input)
    }
    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/slider-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#slider-img-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});

$('#submit-header-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#header-title-input').val()!=''){
        $.ajax({
            url: "/header-submit",
            type: 'POST',
            data: {
                title: $('#header-title-input').val(),
                desc: $('#header-desc-input').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#header-title-input').val('');
                $('#header-desc-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

$('#product-id-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#product-id-input').val()!=''){
        $.ajax({
            url: "/product-id-submit",
            type: 'POST',
            data: {
                pid: $('#product-id-input').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#product-id-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

$('#submit-upslider-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    formdata = new FormData();
    k= parseInt($('#upslider-input').get(0).files.length)
    for (let i = 0; i < k; i++) {
        slider_img_input= ($('#upslider-input'))[0].files[i];
        formdata.append("upslider_img_input", slider_img_input)
    }
    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/upslider-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#upslider-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});

$('#submit-logo-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    formdata = new FormData();
    k= parseInt($('#logo-input').get(0).files.length)
    for (let i = 0; i < k; i++) {
        slider_img_input= ($('#logo-input'))[0].files[i];
        formdata.append("logo_img_input", slider_img_input)
    }
    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/logo-home-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#logo-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});

$('#ad-video-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#ad-video-input').val()!=''){
        $.ajax({
            url: "/ad-video-submit",
            type: 'POST',
            data: {
                url: $('#ad-video-input').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#ad-video-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

$('#submit-insta-pic-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    formdata = new FormData();
    k= parseInt($('#insta-pic-input').get(0).files.length)
    for (let i = 0; i < k; i++) {
        slider_img_input= ($('#insta-pic-input'))[0].files[i];
        formdata.append("insta_img_input", slider_img_input)
    }
    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/insta-pic-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#insta-pic-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});