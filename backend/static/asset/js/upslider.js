$(document).ready(function(){
  var scrollPos = 0;
  var Counter = 0;
  $(".section-container").scroll(function(){
      var scrollPosCur = $(this).scrollTop();
      if (scrollPosCur > scrollPos) {
          Counter -= 1;
      } else {
          Counter += 1;
      }
      scrollPos = scrollPosCur;
    var dot_no = scrollPos / 560
    dot_no = Math.floor( dot_no) + 1;
    var dot = ".dot" + dot_no
        
    $('.dot').removeClass("active");
    $(dot).addClass("active");
  });
});