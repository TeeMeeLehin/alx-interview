#!/usr/bin/node

const request = require('request');

const movie_id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(url, (err, response) => {
    if (err) {
        console.log(err);
    } else if (response.statusCode === 200) {
        const charctrs = JSON.parse(response.body).characters;
        for (const charctr of charctrs) {
            request(charctr, (err, response) => {
                if (err) {
                    console.log(err);
                } else if (response.statusCode === 200) {
                    const name = JSON.parse(response.body).name;
                    console.log(name);
                } else {
                    console.log(response.statusCode);
                }
            })
        };
    } else {
        console.log(response.statusCode);
    }
})
