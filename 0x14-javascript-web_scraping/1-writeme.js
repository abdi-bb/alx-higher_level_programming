#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const stringContent = process.argv[3];

fs.writeFile(filePath, stringContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
