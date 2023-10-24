#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const usersTasks = {};

    for (const task of tasks) {
      if (task.completed) {
        usersTasks[task.userId] = (usersTasks[task.userId] ?? 0) + 1;
      }
    }

    console.log(usersTasks);
  }
});
