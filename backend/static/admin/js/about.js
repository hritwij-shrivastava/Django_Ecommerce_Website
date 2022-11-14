function hide_every_row (){
    $('#slider-row').css({"display":"none"});
    $('#header-row').css({"display":"none"});
    $('#companydata-row').css({"display":"none"});
    $('#vision-row').css({"display":"none"});
    $('#leadership-row').css({"display":"none"});
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

$('#companydata-selector').on('click',function(){
    selector("#companydata-row")
});

$('#vision-selector').on('click',function(){
    selector("#vision-row")
});

$('#leadership-selector').on('click',function(){
    selector("#leadership-row")
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
        url: "/about-slider-submit",
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
            url: "/about-header-submit",
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

$('#submit-companydata-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#title-data1-input').val()!=''){
        $.ajax({
            url: "/about-companydata-submit",
            type: 'POST',
            data: {
                title_data1: $('#title-data1-input').val(),
                data1: $('#value-data1-input').val(),

                title_data2: $('#title-data2-input').val(),
                data2: $('#value-data2-input').val(),

                title_data3: $('#title-data3-input').val(),
                data3: $('#value-data3-input').val(),

                title_data4: $('#title-data4-input').val(),
                data4: $('#value-data4-input').val(),

                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#title-data1-input').val('');
                $('#value-data1-input').val('');

                $('#title-data2-input').val('');
                $('#value-data2-input').val('');

                $('#title-data3-input').val('');
                $('#value-data3-input').val('');

                $('#title-data4-input').val('');
                $('#value-data4-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

$('#submit-vision-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    formdata = new FormData();
    visionImage = ($('#vision-img-input'))[0].files[0];
    vision_desc = $('#vision-desc-input').val();

    formdata.append("visionImage", visionImage);
    formdata.append("vision_desc", vision_desc);

    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/about-vision-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#vision-img-input').val('');
            $('#vision-desc-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});

$('#submit-leadership-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');

    formdata = new FormData();
    leaderImage = ($('#leadership-img-input'))[0].files[0];
    leader_name = $('#leadership-name-input').val();
    leader_designation = $('#leadership-deg-input').val();
    leader_desc = $('#leadership-desc-input').val();
    leader_social_media = $('#leadership-social-input').val();

    formdata.append("leaderImage", leaderImage);
    formdata.append("leader_name", leader_name);
    formdata.append("leader_designation", leader_designation);
    formdata.append("leader_desc", leader_desc);
    formdata.append("leader_social_media", leader_social_media);

    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/about-leadership-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#leadership-img-input').val('');
            $('#leadership-name-input').val('');
            $('#leadership-deg-input').val('');
            $('#leadership-desc-input').val('');
            $('#leadership-social-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});

