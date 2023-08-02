// Wait for the DOM to load before making the AJAX request
$(document).ready(function() {
  // Make the AJAX request to fetch the translation
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      // Display the translation in the <div id="hello">
      $('#hello').text(data.hello);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.error('Error fetching translation:', errorThrown);
    }
  });
});

