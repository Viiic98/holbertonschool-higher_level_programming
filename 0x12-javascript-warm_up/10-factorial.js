#!/usr/bin/node
const n = parseInt(process.argv[2]);
let fact = 1;
if (n) {
  for (let i = 1; i <= n; i++) {
    fact *= i;
  }
  console.log(fact);
} else {
  console.log(fact);
}
