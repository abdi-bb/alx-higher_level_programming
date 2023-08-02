// Wait for the DOM to load before applying changes
$(document).ready(function() {
  // Add event listener for translating when the user clicks on INPUT#btn_translate
  $('#btn_translate').click(function() {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make the AJAX request to fetch the translation
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`,
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Display the translation in the <div id="hello">
        $('#hello').text(data.hello);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error fetching translation:', errorThrown);
        // Display an error message in the <div id="hello">
        $('#hello').text('Error: Translation not found.');
      }
    });
  });
});

