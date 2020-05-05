#!/usr/bin/node
const first = parseInt(process.argv[2]);
if (first) {
  console.log('My number: ' + first);
} else {
  console.log('Not a number');
}
