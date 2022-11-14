$('#modal1').on('hidden.bs.modal', function (e) {
  // do something...
  $('#modal1 iframe').attr("src", $("#modal1 iframe").attr("src"));
});

$('#modal6').on('hidden.bs.modal', function (e) {
  // do something...
  $('#modal6 iframe').attr("src", $("#modal6 iframe").attr("src"));
});

$('#modal4').on('hidden.bs.modal', function (e) {
  // do something...
  $('#modal4 iframe').attr("src", $("#modal4 iframe").attr("src"));
});

// Here I am getting the number of item to display the passing class to myimageslider.js function

$(document).ready(function(){
  $('.carousel-inner').find('.carousel-item:first').addClass('active')

  var masterstart = 1
  if ($(window).width() > 1200) {
    var display_item_no = 4   // set no of item you want to display
  }
  else {
    var display_item_no = 1   // set no of item you want to display
  }
  var masterend = display_item_no 
//<--------------------------------Women Slider Start ----------------------------------->


  var womenstart = masterstart
  var womenend = masterend
  var womencommon_id = ".women-item"
  var womentotalCount = $('.women-item').length
  var womendisplay_item_no = display_item_no
  var womennextBtn_id = '.women-next'
  var womenprevBtn_id = '.women-prev'

  imageSlider(womenstart, womenend, womencommon_id, womentotalCount, womendisplay_item_no, womennextBtn_id, womenprevBtn_id) // function registered in myImageSlider.js

  $(womenprevBtn_id).on('click',function(){

    womenstart = womenstart - 1
    womenend = womenend - 1

    imageSlider(womenstart, womenend, womencommon_id, womentotalCount, womendisplay_item_no, womennextBtn_id, womenprevBtn_id)

  });

  $(womennextBtn_id).on('click',function(){

    womenstart = womenstart + 1
    womenend = womenend + 1

    imageSlider(womenstart, womenend, womencommon_id, womentotalCount, womendisplay_item_no, womennextBtn_id, womenprevBtn_id)

  });

//<--------------------------------Women Slider End ----------------------------------->


//<--------------------------------Men Slider Start ----------------------------------->


var menstart = masterstart
var menend = masterend
var mencommon_id = ".men-item"
var mentotalCount = $('.men-item').length
var mendisplay_item_no = display_item_no
var mennextBtn_id = '.men-next'
var menprevBtn_id = '.men-prev'

imageSlider(menstart, menend, mencommon_id, mentotalCount, mendisplay_item_no, mennextBtn_id, menprevBtn_id) // function registered in myImageSlider.js

$(menprevBtn_id).on('click',function(){

  menstart = menstart - 1
  menend = menend - 1

  imageSlider(menstart, menend, mencommon_id, mentotalCount, mendisplay_item_no, mennextBtn_id, menprevBtn_id)

});

$(mennextBtn_id).on('click',function(){

  menstart = menstart + 1
  menend = menend + 1

  imageSlider(menstart, menend, mencommon_id, mentotalCount, mendisplay_item_no, mennextBtn_id, menprevBtn_id)

});

//<--------------------------------Men Slider End ----------------------------------->

//<--------------------------------Boys Slider Start ----------------------------------->


var boysstart = masterstart
var boysend = masterend
var boyscommon_id = ".boys-item"
var boystotalCount = $('.boys-item').length
var boysdisplay_item_no = display_item_no
var boysnextBtn_id = '.boys-next'
var boysprevBtn_id = '.boys-prev'

imageSlider(boysstart, boysend, boyscommon_id, boystotalCount, boysdisplay_item_no, boysnextBtn_id, boysprevBtn_id) // function registered in myImageSlider.js

$(boysprevBtn_id).on('click',function(){

  boysstart = boysstart - 1
  boysend = boysend - 1

  imageSlider(boysstart, boysend, boyscommon_id, boystotalCount, boysdisplay_item_no, boysnextBtn_id, boysprevBtn_id)

});

$(boysnextBtn_id).on('click',function(){

  boysstart = boysstart + 1
  boysend = boysend + 1

  imageSlider(boysstart, boysend, boyscommon_id, boystotalCount, boysdisplay_item_no, boysnextBtn_id, boysprevBtn_id)

});

//<--------------------------------Boys Slider End ----------------------------------->


//<--------------------------------Girls Slider Start ----------------------------------->


var girlsstart = masterstart
var girlsend = masterend
var girlscommon_id = ".girls-item"
var girlstotalCount = $('.girls-item').length
var girlsdisplay_item_no = display_item_no
var girlsnextBtn_id = '.girls-next'
var girlsprevBtn_id = '.girls-prev'

imageSlider(girlsstart, girlsend, girlscommon_id, girlstotalCount, girlsdisplay_item_no, girlsnextBtn_id, girlsprevBtn_id) // function registered in myImageSlider.js

$(girlsprevBtn_id).on('click',function(){

  girlsstart = girlsstart - 1
  girlsend = girlsend - 1

  imageSlider(girlsstart, girlsend, girlscommon_id, girlstotalCount, girlsdisplay_item_no, girlsnextBtn_id, girlsprevBtn_id)

});

$(girlsnextBtn_id).on('click',function(){

  girlsstart = girlsstart + 1
  girlsend = girlsend + 1

  imageSlider(girlsstart, girlsend, girlscommon_id, girlstotalCount, girlsdisplay_item_no, girlsnextBtn_id, girlsprevBtn_id)

});

//<--------------------------------Girls Slider End ----------------------------------->

//<--------------------------------Logo Slider Start ----------------------------------->


var logostart = masterstart
if ($(window).width() > 1200) {
  var logodisplay_item_no = 7  // set no of item you want to display
}
else {
  var logodisplay_item_no = 2  // set no of item you want to display
}
var logoend = logodisplay_item_no
var logocommon_id = ".logo-item"
var logototalCount = $('.logo-item').length

var logonextBtn_id = '.logo-next'
var logoprevBtn_id = '.logo-prev'

imageSlider(logostart, logoend, logocommon_id, logototalCount, logodisplay_item_no, logonextBtn_id, logoprevBtn_id) // function registered in myImageSlider.js

$(logoprevBtn_id).on('click',function(){

  logostart = logostart - 1
  logoend = logoend - 1

  imageSlider(logostart, logoend, logocommon_id, logototalCount, logodisplay_item_no, logonextBtn_id, logoprevBtn_id)

});

$(logonextBtn_id).on('click',function(){

  logostart = logostart + 1
  logoend = logoend + 1

  imageSlider(logostart, logoend, logocommon_id, logototalCount, logodisplay_item_no, logonextBtn_id, logoprevBtn_id)

});

//<--------------------------------Logo Slider End ----------------------------------->

//<--------------------------------Ad Slider Start ----------------------------------->


var adstart = masterstart
if ($(window).width() > 1200) {
  var addisplay_item_no = 3  // set no of item you want to display
}
else {
  var addisplay_item_no = 1  // set no of item you want to display
}
var adend = addisplay_item_no
var adcommon_id = ".ad-item"
var adtotalCount = $('.ad-item').length

var adnextBtn_id = '.ad-next'
var adprevBtn_id = '.ad-prev'

imageSlider(adstart, adend, adcommon_id, adtotalCount, addisplay_item_no, adnextBtn_id, adprevBtn_id) // function registered in myImageSlider.js

$(adprevBtn_id).on('click',function(){

  adstart = adstart - 1
  adend = adend - 1

  imageSlider(adstart, adend, adcommon_id, adtotalCount, addisplay_item_no, adnextBtn_id, adprevBtn_id)

});

$(adnextBtn_id).on('click',function(){

  adstart = adstart + 1
  adend = adend + 1

  imageSlider(adstart, adend, adcommon_id, adtotalCount, addisplay_item_no, adnextBtn_id, adprevBtn_id)

});

//<--------------------------------Ad Slider End ----------------------------------->

});
