#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code: ' + response.statusCode);
});
