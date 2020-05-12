#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];

// Function that reads a file
function rFile (file) {
  fs.readFile(file, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    console.log(data);
  });
}
rFile(file);
