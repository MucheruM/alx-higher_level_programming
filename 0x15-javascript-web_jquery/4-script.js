// Toggles <header> when clicking DIV#toggle_header

$('div#toggle_header').on('click', () => {
    $('header').toggleClass('green red');
});
