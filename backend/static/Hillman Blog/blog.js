



CKEDITOR.disableAutoInline = true;

CKEDITOR.inline('area', {
sharedSpaces: {
    top: 'top',
    bottom: 'bottom'
}
});

$(document).ready( function(){
   

    var base_url = $('#home-link').attr('href');
    var id = $('.main-area').attr('id');

    $('.selector-shadow').hover(function(){
        $(this).removeClass('shadow');
        },function(){
            $(this).addClass('shadow'); 
        }
    );


    $('#upnav').on('click' ,function(){
        $('.mynav').addClass('hideall');
        $('#downnav').addClass('showdown');
        $('#upnav').addClass('hideup');
        $('#top').addClass('sticky-top');
    });
    $('#downnav').on('click' ,function(){
        $('.mynav').removeClass('hideall');
        $('#upnav').removeClass('hideup');
        $('#downnav').removeClass('showdown');
        $('#top').removeClass('sticky-top');
    });
    $("#input-h").focusin(function() {
        $( "#title-h" ).addClass( "newone" );
    }).focusout(function () {
        $( "#title-h" ).removeClass( "newone" );
    });
    // $('#file-img-input').change(function(e){
    //     $val_file = e.target.files[0].name;
    //     alert($val_file)
    // });
    $('#area').keyup(function (){
        $.ajax({
            url: base_url +  "/my-adminpage/edit/upload",
            type: "POST",
            dataType:'json',
            data: {
              id:id,
              title:$("#input-h").val(),
              content:CKEDITOR.instances.area.getData(),
              simple_post:$("#simple_post").val(),
              status:0,
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
              action: 'post'
            },
            success: function (data) {
                // console.log(CKEDITOR.instances.area.getData())
            }
        }); 
    });
    $('#input-h').keyup(function (){
        $.ajax({
            url: base_url +  "/my-adminpage/edit/upload",
            type: "POST",
            dataType:'json',
            data: {
              id:id,
              title:$("#input-h").val(),
              content:CKEDITOR.instances.area.getData(),
              simple_post:$("#simple_post").val(),
              status:0,
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
              action: 'post'
            },
            success: function (data) {
                // console.log(CKEDITOR.instances.area.getData())
            }

        }); 
    });
    $('#simple_post').keyup(function (){
        formdata = new FormData();

        title = $("#input-h").val()
        content = CKEDITOR.instances.area.getData()
        simple_post = $("#simple_post").val()
        status = 0
        formdata.append("title", title);
        formdata.append("id", id);
        formdata.append("action", 'post');
        formdata.append("content", content);
        formdata.append("simple_post", simple_post);
        formdata.append("status", status);
        formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
        k= parseInt($('#file-img-input').get(0).files.length)
        if(k==1){
            thumbnail_img= ($('#file-img-input'))[0].files[0];
            formdata.append("thumbnail_img", thumbnail_img)
        }
        $.ajax({
            url: base_url +  "/my-adminpage/edit/upload",
            type: "POST",
            contentType: false,
            processData: false,
            data: formdata,
            success: function (data) {
                // console.log(CKEDITOR.instances.area.getData())
            }
        }); 
    });
    $('#post-publish-final').on('click',function (){
        $('.loader-animate').removeClass('loader-hide');
        formdata = new FormData();

        title = $("#input-h").val()
        content = CKEDITOR.instances.area.getData()
        simple_post = $("#simple_post").val()
        status = 1
        thumbnail_img = ($('#file-img-input'))[0].files[0];

        formdata.append("title", title);
        formdata.append("id", id);
        formdata.append("action", 'post');
        formdata.append("content", content);
        formdata.append("simple_post", simple_post);
        formdata.append("status", status);
        formdata.append("thumbnail_img", thumbnail_img)

        formdata.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
        
        $.ajax({
            url: base_url +  "/my-adminpage/edit/finalupload",
            type: "POST",
            contentType: false,
            processData: false,
            data: formdata,
            success: function (data) {
                $('.loader-animate').addClass('loader-hide'); 
                setTimeout(function(){
                    alert('Blog Published Succeessfully')
                    location.replace( base_url +  "/my-adminpage/blog")
                },500);  
            }
        }); 
    });
    CKEDITOR.on('dialogDefinition', function(e){
        dialogName = e.data.name;
        dialogDefinition = e.data.definition;
        //console.log(dialogName);
        //console.log(dialogDefinition);
        if(dialogName == 'image') {

            var dialog = CKEDITOR.dialog.getCurrent();

            var uploadTab = dialogDefinition.getContents('Upload');
            var uploadButton = uploadTab.get('uploadButton');
            console.log('uploadButton', uploadButton);

            uploadButton['onClick'] = function(evt){
                alert("Hello! I am an alert box!!");
            }

            dialogDefinition.dialog.resize( 300, 200 );
            dialogDefinition.resizable = CKEDITOR.DIALOG_RESIZE_NONE;
            dialogDefinition.removeContents('Link');
            dialogDefinition.removeContents('advanced');
            var infocontent = dialogDefinition.getContents('info');
            infocontent.remove('txtHSpace');
            infocontent.remove('txtVSpace');
            infocontent.remove('txtWidth');
            infocontent.remove('txtHeight');
            infocontent.remove('txtBorder');
            infocontent.remove('cmbAlign');
            infocontent.remove('ratioLock');
            infocontent.remove('htmlPreview');
            infocontent.remove('txtAlt');
        }
    })




});
function goBack() {
    window.history.back();
}
function mypost(){
    // window.history.back();
}