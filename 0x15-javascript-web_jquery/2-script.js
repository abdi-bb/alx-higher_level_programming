// Wait for the DOM to load before applying changes
$(document).ready(function() {
  // Attach a click event listener to the DIV#red_header element
  $('#red_header').click(function() {
    // Update the text color of the <header> element to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});

