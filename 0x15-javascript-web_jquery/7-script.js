const characterDiv = $('DIV#character');

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (response) {
  characterDiv.text(response.name);
});
