#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const file = process.argv[3];

request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  // Parse string body response to an object
  if (response.statusCode === 200) {
    // Write in the file
    fs.writeFile(file, body, (err) => {
      if (err) throw err;
    });
  }
});
