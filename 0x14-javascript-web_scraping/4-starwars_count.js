#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const count = body.split('/people/18/').length - 1;
    console.log(count);
  }
});
