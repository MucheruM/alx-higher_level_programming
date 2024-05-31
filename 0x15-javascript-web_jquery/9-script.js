// Fetches from a URL and display hello from DIV#hello
// The translation of "hello" must be displayed in the DIV#hello

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, (data) => {
    $('div#hello').text(data.hello);
});
