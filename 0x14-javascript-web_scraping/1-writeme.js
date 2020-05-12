#!/usr/bin/node
const fs = require('fs');

const dest = process.argv[2];
const data = process.argv[3];

// Write in the file
fs.writeFile(dest, data, (err) => {
  if (err) throw err;
});
