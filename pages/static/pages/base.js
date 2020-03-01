$(".menu-toggle-btn").click(function(){
  $(this).toggleClass("fa-times");
  $(".navigation-menu").toggleClass("active");
});

const mql = matchMedia("screen and (min-width: 700px");

function response(mql){
  if(mql.matches){
    $(".menu-toggle-btn").removeClass("fa-times");
    $(".navigation-menu").removeClass("active");
  }
}

mql.addListener(response);
response(mql);

