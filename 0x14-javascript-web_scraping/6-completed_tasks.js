#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  // Parse string body response to an object
  if (response.statusCode < 400) {
    const obj = JSON.parse(body);
    const userTasks = {};
    for (let i = 0; i < obj.length; i++) {
      const userId = String(obj[i].userId);
      if (userTasks[userId]) {
        userTasks[userId]++;
      } else {
        userTasks[userId] = 1;
      }
    }
    console.log(userTasks);
  }
});
