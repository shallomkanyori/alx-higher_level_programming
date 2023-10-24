#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const personUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const count = body.split(personUrl).length - 1;
    console.log(count);
  }
});
