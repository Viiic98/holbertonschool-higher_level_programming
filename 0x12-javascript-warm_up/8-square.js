#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!x) {
  console.log('Missing size');
} else {
  let i, j;
  for (i = 0; i < x; i++) {
    let sqr = '';
    for (j = 0; j < x; j++) {
      sqr += 'X';
    }
    console.log(sqr);
  }
}
