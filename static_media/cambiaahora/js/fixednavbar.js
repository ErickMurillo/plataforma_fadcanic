$(document).ready(main);

function main(){
	  $(window).scroll(function() {
        if ($(window).scrollTop() >= $("#header").height()) {   //alto del header
        	$('.navbar').css({'z-index':'15000', 'position':'fixed','top':'0px', 'width':'100%'});
        } else {
          $('.navbar').css({'z-index':'100','position':'relative','top':'auto'});          
        }
      });
}

$(window).scroll(function() {
    if ($(".navbar").offset().top > 500) {
        $(".navbar").addClass("menu-fixed");


       
    } else {
        $(".navbar").removeClass("menu-fixed");

    }
});