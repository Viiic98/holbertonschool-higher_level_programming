#!/usr/bin/node
const fs = require('fs');

const first = process.argv[2];
const second = process.argv[3];
const dest = process.argv[4];

// Function that reads a file
function rFile (file) {
  try {
    const data = fs.readFileSync(file, 'utf8');
    return (data);
  } catch (err) {
    console.error(err);
    return '';
  }
}
// Store the information of every file
let data = rFile(first) + '\n';
data += rFile(second) + '\n';

// Write in the file
fs.writeFile(dest, data, (err) => {
  if (err) throw err;
});
