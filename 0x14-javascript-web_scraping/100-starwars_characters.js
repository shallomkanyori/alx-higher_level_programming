#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const printCharacter = function (charUrl) {
  request(charUrl, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const person = JSON.parse(body);
      console.log(person.name);
    }
  });
};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    for (const charUrl of movie.characters) {
      printCharacter(charUrl);
    }
  }
});
