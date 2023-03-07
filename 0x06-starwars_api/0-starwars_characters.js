#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (movieId <= 6) {
  // Make a GET request to the Star Wars API films endpoint
  request(`https://swapi.dev/api/films/${movieId}`, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
    } else {
      // Parse the JSON response
      const data = JSON.parse(body);

      // Get the list of character URLs from the response
      const characterUrls = data.characters;

      // Iterate through the character URLs and make a GET request for each one
      characterUrls.forEach((url) => {
        request(url, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else if (response.statusCode !== 200) {
            console.error('Unexpected status code:', response.statusCode);
          } else {
            // Parse the JSON response and print the character name
            const data = JSON.parse(body);
            console.log(data.name);
          }
        });
      });
    }
  });
} else {
  console.log('no movies with that id');
}
