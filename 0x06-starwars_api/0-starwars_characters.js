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
      request(charctr, (err, res) => {
        if (err) {
          console.log(err);
        } else if (res.statusCode === 200) {
          const name = JSON.parse(res.body).name;
          console.log(name);
        } else {
          console.log(res.statusCode);
        }
      });
    });
  } else {
    console.log(response.statusCode);
  }
});
