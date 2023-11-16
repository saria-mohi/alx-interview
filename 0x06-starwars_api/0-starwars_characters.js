#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const req = require('request');

req.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, res, body) {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  // Use async/await to ensure names are printed in the correct order
  (async () => {
    for (const i of dd) {
      try {
        const characterData = await fetchCharacterData(i);
        console.log(characterData.name);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }
  })();
  // Function to fetch character data
  async function fetchCharacterData (url) {
    return new Promise((resolve, reject) => {
      req.get(url, function (error, res, body1) {
        if (error) {
          reject(error);
        }
        const data1 = JSON.parse(body1);
        resolve(data1);
      });
    });
  }
});
