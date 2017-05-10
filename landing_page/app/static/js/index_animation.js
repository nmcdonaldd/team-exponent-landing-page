

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

// $(document).ready(function() {
//     function ani() {
//         $('#divers').animate({
//                'margin-top':'90px'
//             },6000).animate({
//                'margin-top':'40px'
//            },6000, ani); //call the function again in the callback
//         });
//     });
//     ani();
// });

/*window.onload = function() {
  if (window.jQuery) {
      $("*").fadeIn(2000);
      alert("Yeah!");
  } else {
      // jQuery is not loaded
      alert("Doesn't Work");
  }
}*/
