#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const charctrs = JSON.parse(response.body).characters;
    charctrs.forEach(charctr => {
      request(charctr, (err, response) => {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          const name = JSON.parse(response.body).name;
          console.log(name);
        } else {
          console.log(response.statusCode);
        }
      });
    });
  } else {
    console.log(response.statusCode);
  }
});
