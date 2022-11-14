$('#submit-to-sheet').submit(function(e){
    e.preventDefault();
    var ipinfo;
    $.getJSON("https://api.ipify.org?format=json", function (data) {
        ipinfo = data.ip;
    })
    $('.loader-animate').removeClass('loader-hide');
    uname = $('#User_name').val();
    email = $('#email').val();
    phone = $('#phone').val();
    message = $('#message').val();
    if($('#uname').val()!=''){
        $.ajax({
            url: "/contact-user-submit",
            type: 'POST',
            data: {
                status: 1,
                name: uname,
                email: email,
                phone: phone,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
    
            success: function(json){
                $('.loader-animate').addClass('loader-hide');
                
                const scriptURL = json.url;
               
                formdata = new FormData();
                formdata.append("User_ip", ipinfo);
                formdata.append("User_name", uname);
                formdata.append("email", email);
                formdata.append("phone", phone);
                formdata.append("message", message);

                fetch(scriptURL, { method: 'POST', body: formdata})
                .then(response => console.log('Success!', response,'ip:'+ipinfo))
                .catch(error => console.error('Error!', error.message))
                alert(json.title);
                $('#User_name').val('');
                $('#email').val('');
                $('#phone').val('');
                $('#message').val('');
                
            }
    
        });
    }
});
