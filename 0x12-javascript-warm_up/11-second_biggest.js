#!/usr/bin/node
const nArgs = process.argv.length;
if (nArgs > 3) {
  let biggest = 0;
  let secBig = 0;
  for (let i = 2; i < nArgs; i++) {
    const n = parseInt(process.argv[i]);
    if (n > biggest) {
      secBig = biggest;
      biggest = n;
    }
    if (n > secBig && n < biggest) {
      secBig = n;
    }
  }
  console.log(secBig);
} else {
  console.log(0);
}
