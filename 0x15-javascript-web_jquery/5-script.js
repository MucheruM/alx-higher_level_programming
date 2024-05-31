// Add <li> element to a list
// When the user clicks DIV#add_item

$('div#toggle_header').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
});
