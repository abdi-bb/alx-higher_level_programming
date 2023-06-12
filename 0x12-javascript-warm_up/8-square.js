#!/usr/bin/node
const size = process.argv[2];
const num = parseInt(size);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  if (num > 0) {
    const line = 'X'.repeat(num);
    for (let i = 0; i < num; i++) {
      console.log(line);
    }
  }
}
