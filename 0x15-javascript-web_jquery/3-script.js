// Wait for the DOM to load before applying changes
$(document).ready(function() {
  // Attach a click event listener to the DIV#red_header element
  $('#red_header').click(function() {
    // Add the class "red" to the <header> element
    $('header').addClass('red');
  });
});

