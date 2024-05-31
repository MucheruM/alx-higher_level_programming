// Update the text of the <header> to 'New Header!!!'
// When the user clicks on DIV#update_header

$('div#update_header').on('click', () => {
    $('header').text('New Header!!!');
});
