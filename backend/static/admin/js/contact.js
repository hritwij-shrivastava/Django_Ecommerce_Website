function hide_every_row (){
    $('#contact-info-row').css({"display":"none"});
    $('#user-message-row').css({"display":"none"});
    $('#footer-about-row').css({"display":"none"});
    $('#footer-category-row').css({"display":"none"});
    $('#footer-useful-row').css({"display":"none"});
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

    selector("#contact-info-row")
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

$('#contact-info-selector').on('click',function(){
    selector("#contact-info-row")
});

$('#user-message-selector').on('click',function(){
    selector("#user-message-row")
});

$('#footer-about-selector').on('click',function(){
    selector("#footer-about-row")
});

$('#footer-category-selector').on('click',function(){
    selector("#footer-category-row")
});

$('#footer-useful-selector').on('click',function(){
    selector("#footer-useful-row")
});


$('#submit-contact-info-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');

    formdata = new FormData();
    background_img = ($('#bkg-img-input'))[0].files[0];
    address = $('#address-input').val();
    phoneNo = $('#phoneno-input').val();
    email_id = $('#email-id-input').val();
    workingHour1 = $('#workinghour-one-input').val();
    workingHour2 = $('#workinghour-two-input').val();
    facebook_url = $('#facebook-input').val();
    twitter_url = $('#twitter-input').val();
    insta_url = $('#insta-input').val();
    linkedin_url = $('#linkedin-input').val();

    formdata.append("background_img", background_img);
    formdata.append("address", address);
    formdata.append("phoneNo", phoneNo);
    formdata.append("email_id", email_id);
    formdata.append("workingHour1", workingHour1);
    formdata.append("workingHour2", workingHour2);
    formdata.append("facebook_url", facebook_url);
    formdata.append("twitter_url", twitter_url);
    formdata.append("insta_url", insta_url);
    formdata.append("linkedin_url", linkedin_url);

    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

    $.ajax({
        url: "/contact-info-submit",
        type: 'POST',
        contentType: false,
        processData: false,
        data: formdata,
            
        success: function(json){
            $('#bkg-img-input').val('');
            $('#address-input').val('');
            $('#phoneno-input').val('');
            $('#email-id-input').val('');
            $('#workinghour-one-input').val('');
            $('#workinghour-two-input').val('');
            $('#facebook-input').val('');
            $('#twitter-input').val('');
            $('#insta-input').val('');
            $('#linkedin-input').val('');

            $('.loader-animate').addClass('loader-hide');
            alert(json.title)
        }

    });

});

$('#submit-footer-about-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#title-data1-input').val()!=''){
        $.ajax({
            url: "/footer-about-submit",
            type: 'POST',
            data: {
                title: $('#title-data1-input').val(),
                url: $('#value-data1-input').val(),

                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#title-data1-input').val('');
                $('#value-data1-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

$('#submit-footer-category-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#title-data2-input').val()!=''){
        $.ajax({
            url: "/footer-category-submit",
            type: 'POST',
            data: {
                title: $('#title-data2-input').val(),
                url: $('#value-data2-input').val(),

                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#title-data2-input').val('');
                $('#value-data2-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }

});

$('#submit-footer-useful-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#title-data1-input3').val()!=''){
        $.ajax({
            url: "/footer-useful-submit",
            type: 'POST',
            data: {
                title: $('#title-data3-input').val(),
                url: $('#value-data3-input').val(),

                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){

                $('#title-data3-input').val('');
                $('#value-data3-input').val('');

                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }

});

