#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const personUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    let count = 0;

    for (const movie of movies) {
      if (movie.characters.indexOf(personUrl) >= 0) {
        count++;
      }
    }

    console.log(count);
  }
});
