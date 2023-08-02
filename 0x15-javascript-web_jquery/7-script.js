// Wait for the DOM to load before making the AJAX request
$(document).ready(function() {
  // Make the AJAX request to fetch the character data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      // Update the text of the <div id="character"> with the character name
      $('#character').text(data.name);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.error('Error fetching character data:', errorThrown);
    }
  });
});
