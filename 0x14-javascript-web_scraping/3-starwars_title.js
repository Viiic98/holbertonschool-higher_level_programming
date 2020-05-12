#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  // Parse string body response to an object
  if (response.statusCode < 400) {
    const obj = JSON.parse(body);
    if (obj) {
      console.log(obj.title);
    }
  }
});
