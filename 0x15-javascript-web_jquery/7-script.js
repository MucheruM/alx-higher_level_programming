// Fetch the character name from the given URL
// The name must be displayed in the DIV#character

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, (data, status) => {
    if (status === 'success') {
	$('#character').append(data.name);
    }
});
