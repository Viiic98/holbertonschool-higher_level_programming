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
        const charList = moviesList[i].characters;
        for (let j = 0; j < charList.length; j++) {
          if (charList[j].endsWith('/18/')) {
            nMovies++;
          }
        }
      }
      console.log(nMovies);
    }
  }
});
