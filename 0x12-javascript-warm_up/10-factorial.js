#!/usr/bin/node
function fact (n) {
  if (n === 1) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
const n = parseInt(process.argv[2]);
if (n) {
  console.log(fact(n));
} else {
  console.log(1);
}
