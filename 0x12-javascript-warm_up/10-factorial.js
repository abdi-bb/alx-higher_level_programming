#!/usr/bin/node

function fact (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  return a * fact(a - 1);
}

const arg = process.argv[2];
const num = parseInt(arg);

console.log(fact(num));
