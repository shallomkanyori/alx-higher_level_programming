const movieList = $('UL#list_movies');

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  for (const movie of response.results) {
    const item = $('<li></li>').text(movie.title);
    movieList.append(item);
  }
});
