## JavaScript - Web scraping

#### Task 0
[0-readme.js](0-readme.js) is a JS script that reads and prints the content of a file.
- The first argument is the file path
- The content of the file is read in `utf-8`
- If an error occurred during the reading, prints the error object

#### Task 1
[1-writeme.js](1-writeme.js) is a JS script that writes a string to a file.
- The first argument is the file path
- The second argument is the string to write
- The content of the file is written in `utf-8`
- If an error occurred during while writing, prints the error object

#### Task 2
[2-statuscode.js](2-statuscode.js) is a JS script that display the status code of a GET request.
- The first argument is the URL to request (`GET`)
- The status code is printed as: `code: <status code>`
- Uses the module `request`

#### Task 3
[3-starwars_title.js](3-starwars_title.js) is a JS script that prints the title of a Star Wars movie where the episode number matches a given integer.
- The first argument is the movie ID
- Uses the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- Uses the module `request`
