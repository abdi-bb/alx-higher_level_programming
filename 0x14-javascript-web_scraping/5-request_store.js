#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, res, bod) => {
  if (!err) {
    if (res.statusCode === 200) {
      fs.writeFile(filePath, bod, 'utf8', (err) => {
        if (err) {
          console.log(err.message);
        }
      });
    }
  }
});
