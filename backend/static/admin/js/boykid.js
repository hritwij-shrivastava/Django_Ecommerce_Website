
// $('.product-list').on('change', function() {
//     $('.product-list').not(this).prop('checked', false);  
//     $('#editctg').removeClass('disabled');
//     $('#deletectg').removeClass('disabled');
// });


// for category section 
$(document).ready(function(){
    $('.selector-shadow').hover(function(){
        $(this).removeClass('shadow');
        },function(){
            $(this).addClass('shadow'); 
        }
    );
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

$('#category-selector').on('click',function(){
    $('#category-row').css({"display":""});
    $('#brand-row').css({"display":"none"});
    $('#tags-row').css({"display":"none"});
    $('#product-row').css({"display":"none"});
});
$('#brand-selector').on('click',function(){
    $('#category-row').css({"display":"none"});
    $('#brand-row').css({"display":""});
    $('#tags-row').css({"display":"none"});
    $('#product-row').css({"display":"none"});
});
$('#tags-selector').on('click',function(){
    $('#category-row').css({"display":"none"});
    $('#brand-row').css({"display":"none"});
    $('#tags-row').css({"display":""});
    $('#product-row').css({"display":"none"});
});
$('#product-selector').on('click',function(){
    $('#category-row').css({"display":"none"});
    $('#tags-row').css({"display":"none"});
    $('#brand-row').css({"display":"none"});
    $('#product-row').css({"display":""});
});
$('#submit-category-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#category-text-input').val()!=''){
    
        $.ajax({
            url: "/boys-m-category-submit",
            type: 'POST',
            data: {
                category: $('#category-text-input').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },

            success: function(json){
                $('#category-text-input').val('');
                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }

        });
    }
});

// for brand section 

$('#submit-brand-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#brand-text-input').val()!=''){
        brand= $('#brand-text-input').val();
        brand_img= ($('#brand-img-input'))[0].files[0];
        formdata = new FormData();	
        formdata.append("brand", brand);
        formdata.append("brand_img", brand_img);
        formdata.append("action", 'post');
        formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
        $.ajax({
            url: "/boys-m-brand-submit",
            type: 'POST',
            contentType: false,
            processData: false,
            data: formdata,

            success: function(json){
                $('#brand-text-input').val('');
                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

// for tag section 

$('#submit-tags-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');
    if($('#tags-text-input').val()!=''){
        $.ajax({
            url: "/boys-m-tags-submit",
            type: 'POST',
            data: {
                tags: $('#tags-text-input').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('#tags-text-input').val('');
                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

// for product section

$('#product-img-no-input').on('input',function(){
    k = $('#product-img-no-input').val();
    if(k<0 || k>15){
        $('#validationServer03Feedback').css({"display": "block"});
        $('#product-img-no-input').addClass("is-invalid");
    }
    else{
        $('#validationServer03Feedback').css({"display": "none"});
        $('#product-img-no-input').removeClass("is-invalid");
    }
});

$('#product-opt-img-input').change(function(){
    k = parseInt($('#product-opt-img-input').get(0).files.length);
    
    if (k > 15){
        $('#validationServer04Feedback').css({"display": "block"});
        $('#validationServer04Feedback').append("<p>You are only allowed to upload a maximum of " + "15" + " files</p>");
        $('#product-opt-img-input').val('');
    }
    else{
        $('#product-img-no-input').val(k);
        $('#validationServer04Feedback').css({"display": ""});
    }
});


$('#submit-product-form').submit(function(e){
    e.preventDefault();
    $('.loader-animate').removeClass('loader-hide');

    formdata = new FormData();

    product_name= $('#product-name-input').val();
    product_id= $('#product-id-input').val();
    product_ctg= $('#product-ctg-input').val();
    product_brand= $('#product-brand-input').val();
    product_tags= $('#product-tags-input').val();
    var size = [];
       $('.ads_Checkbox:checked').each(function () {
           size.push($(this).val());
       });
    product_spec= $('#product-spec-input').val();
    product_color= $('#product-desc-input').val();
    product_img= ($('#product-img-input'))[0].files[0];
    
    k= parseInt($('#product-opt-img-input').get(0).files.length)
    product_img_no= k

    for (let i = 0; i < k; i++) {
        product_opt_img= ($('#product-opt-img-input'))[0].files[i];
        formdata.append("product_opt_img", product_opt_img)
    }

    	
    formdata.append("product_name", product_name);
    formdata.append("product_id", product_id);
    formdata.append("product_ctg", product_ctg);
    formdata.append("product_brand", product_brand);
    formdata.append("product_tags", product_tags);
    formdata.append("product_color", product_color);
    formdata.append("size", size);
    formdata.append("product_spec", product_spec);
    formdata.append("product_img", product_img);
    formdata.append("product_img_no", product_img_no);
    formdata.append("action", 'post');
    formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    
    if($('#product-name-input').val()!=''){
        $.ajax({
            url: "/boys-m-product-submit",
            type: 'POST',
            contentType: false,
            processData: false,
            data: formdata,
                
            success: function(json){
                $('#product-name-input').val('');
                $('#product-id-input').val('');
                $('#product-ctg-input').val('');
                $('#product-brand-input').val('');
                $('#product-tags-input').val('');
                $('#product-spec-input').val('');
                $('#product-desc-input').val('');
                $('.ads_Checkbox:checked').prop('checked', false);
                $('#product-img-input').val('');
                $('#product-img-no-input').val('0');
                $('#product-opt-img-input').val('');
                $('.loader-animate').addClass('loader-hide');
                alert(json.title)
            }
    
        });
    }
});

