// This function counts number of product using class and display n number of product when clicking on next button 1st product 
//will display none and next product will display block


function imageSlider(start, end, common_id, totalCount, display_item_no, nextBtn_id, prevBtn_id){

  if(start >= 1 && end <= totalCount && end - start == display_item_no -1 ){

    $(common_id).css("display","none")

    for(var i = start; i < end+1; i++){
      var bid = common_id +":nth-child(" + i + ")"
      $(bid).css("display","block")
    }

    if(end == totalCount){
      $(nextBtn_id).css("opacity","0")
    }
    else{
      $(nextBtn_id).css("opacity","1")
    }
    if(start == 1){
      $(prevBtn_id).css("opacity","0")
    }
    else{
      $(prevBtn_id).css("opacity","1")
    }

  }

}
