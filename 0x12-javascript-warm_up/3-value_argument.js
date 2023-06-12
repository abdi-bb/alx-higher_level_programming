#!/usr/bin/node
const argsArray = process.argv;

if (!argsArray[2]) {
  console.log('No argument');
} else {
  console.log(argsArray[2]);
}
