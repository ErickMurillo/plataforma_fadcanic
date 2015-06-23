  (function($) {

  /**
   * jQuery function to prevent default anchor event and take the href * and the title to make a share pupup
   *
   * @param  {[object]} e           [Mouse event]
   * @param  {[integer]} intWidth   [Popup width defalut 500]
   * @param  {[integer]} intHeight  [Popup height defalut 400]
   * @param  {[boolean]} blnResize  [Is popup resizeabel default true]
   */
  $.fn.customerPopup = function(e, intWidth, intHeight, blnResize) {

    // Prevent default anchor event
    e.preventDefault();

    // Set values for window
    intWidth = intWidth || '500';
    intHeight = intHeight || '400';
    strResize = (blnResize ? 'yes' : 'no');

    // Set title and open popup with focus on it
    var strTitle = ((typeof this.attr('title') !== 'undefined') ? this.attr('title') : 'Social Share'),
      strParam = 'width=' + intWidth + ',height=' + intHeight + ',resizable=' + strResize,
      objWindow = window.open(this.attr('href'), strTitle, strParam).focus();
  }

  /* ================================================== */

  $(document).ready(function($) {
    $('.customer.share').on("click", function(e) {
      $(this).customerPopup(e);
    });
  });

$(document).ready(function() {
        var posicion = $("#share-buttons").offset();
      var margenSuperior = 150;
       $(window).scroll(function() {
           if ($(window).scrollTop() > posicion.top) {
               $("#share-buttons").stop().animate({
                   marginTop: $(window).scrollTop() - posicion.top + margenSuperior
               });
           } else {
               $("#share-buttons").stop().animate({
                   marginTop: 100
               });
           };
       });
});
}(jQuery));

