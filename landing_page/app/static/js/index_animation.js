$(document).ready(function(){
    //console.log("pls");

    $("#welcome").hide().fadeIn(2000);
    $(".slogan").hide().fadeIn(3000);

    $("#subscribe-content").hide();
    $("#why-content").hide();
    $("#what-content").show();
    $("#login-form").hide();

    $("#login-button").click(function() {
    //$("#what-button").click(function() {
      console.log("click");
      $("#subscribe-content").hide(1000);
      $("#why-content").hide(1000);
      $("#what-content").show(1000);
    });

    $("#why-button").click(function() {
      console.log("click2");
      $("#subscribe-content").hide(1000);
      $("#why-content").show(1000);
      $("#what-content").hide(1000);
    });

    $("#subscribe-button").click(function() {
      console.log("clic3242342434k2");
      $("#subscribe-content").show(1000);
      $("#why-content").hide(1000);
      $("#what-content").hide(1000);
    });

    $("#login-button").click(function() {
      console.log("login yo");
      //$("#login-modal").modal('show');
      $("#login-modal").show(1000);
      $("#subscribe-content").hide(1000);
      $("#why-content").hide(1000);
      $("#what-content").hide(1000);
    });

    function start() {
      $("body").animate({
      'background-position-x': '15%',
      'background-position-y': '25%'
      }, 10000, 'linear', function() {
          $("body").animate({
          'background-position-x': '-15%',
          'background-position-y': '-25%'
        }, 10000, 'linear', start);
      });
    }

    start();
});
