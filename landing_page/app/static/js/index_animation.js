$(document).ready(function(){
    console.log("pls");
    $("#welcome").hide().fadeIn(2000);
    $(".slogan").hide().fadeIn(3000);


    function start() {
      console.log("wat");
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
