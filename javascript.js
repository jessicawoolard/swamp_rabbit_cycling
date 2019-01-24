$(document).ready(function() {
  $('.toggle').hide();
  $('#carousel-example').on('slide.bs.carousel', function () {
    var menu = $(this).find('.item.active').data("menu");
    $('#' + menu).show();
  })
});