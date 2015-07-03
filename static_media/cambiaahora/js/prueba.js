	// Flexsliderfunction function
		$(window).load(function() {
			if($('.flexslider').length){
			
		$('.testimonial .flexslider').flexslider({
			animation : "slide",
			animationLoop : false,
			itemWidth :360,
			itemMargin : 30,
			slideToStart: 0,
			move:1,

			start : function(slider) {
				$('body').removeClass('loading');
			}
		});
		
			$('.testimonial .flexslider, .donation-holder .flexslider,.flex-slide.flexslider').flexslider({
				
			animation : "slide",
			animationLoop : false
			
		});
		}
		
	});