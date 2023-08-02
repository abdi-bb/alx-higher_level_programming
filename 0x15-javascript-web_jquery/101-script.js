// Wait for the DOM to load before applying changes
$(document).ready(function() {
  // Add event listener for adding a new item
  $('#add_item').click(function() {
    // Create a new <li> element with the content "Item"
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the UL.my_list
    $('ul.my_list').append(newItem);
  });

  // Add event listener for removing the last item
  $('#remove_item').click(function() {
    // Select the last <li> element within UL.my_list and remove it
    $('ul.my_list li:last-child').remove();
  });

  // Add event listener for clearing the entire list
  $('#clear_list').click(function() {
    // Remove all <li> elements from the UL.my_list
    $('ul.my_list').empty();
  });
});

