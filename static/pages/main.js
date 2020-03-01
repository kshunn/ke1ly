$(".menu-toggle-btn").click(function(){
  $(this).toggleClass("fa-times");
  $(".navigation-menu").toggleClass("active");
});


$(".owl-carousel").owlCarousel({
  items: 2,
  margin: 20,
  loop: true,
  center: true,
  dots: false
});
