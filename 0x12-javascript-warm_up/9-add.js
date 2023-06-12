#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

if (num1 && num2) {
  add(num1, num2);
} else {
  console.log('NaN');
}
