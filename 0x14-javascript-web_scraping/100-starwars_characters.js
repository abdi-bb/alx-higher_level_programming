#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (err, res, bod) => {
  if (!err) {
    const characters = JSON.parse(bod).characters;
    for (let i = 0; i < characters.length; ++i) {
      request(characters[i], (cErr, cRes, cBod) => {
        if (!cErr) {
          console.log(JSON.parse(cBod).name);
        }
      });
    }
  }
});
