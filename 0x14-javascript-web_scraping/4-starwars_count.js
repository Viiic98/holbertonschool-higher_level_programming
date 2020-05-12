#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
request(URL, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  }
  // Parse string body response to an object
  if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    if (obj) {
      const moviesList = obj.results;
      let nMovies = 0;
      for (let i = 0; i < moviesList.length; i++) {
        if (moviesList[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
          nMovies++;
        }
      }
      console.log(nMovies);
    }
  }
});
