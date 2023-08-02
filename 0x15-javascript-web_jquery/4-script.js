// Wait for the DOM to load before applying changes
$(document).ready(function() {
  // Attach a click event listener to the DIV#toggle_header element
  $('#toggle_header').click(function() {
    // Check the current class of the <header> element
    if ($('header').hasClass('red')) {
      // If the current class is red, remove it and add the green class
      $('header').removeClass('red').addClass('green');
    } else {
      // If the current class is green, remove it and add the red class
      $('header').removeClass('green').addClass('red');
    }
  });
});

