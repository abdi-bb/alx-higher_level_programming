// Wait for the DOM to load before applying changes
$(document).ready(function() {
  // Attach a click event listener to the DIV#add_item element
  $('#add_item').click(function() {
    // Create a new <li> element with the content "Item"
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the UL.my_list
    $('ul.my_list').append(newItem);
  });
});

