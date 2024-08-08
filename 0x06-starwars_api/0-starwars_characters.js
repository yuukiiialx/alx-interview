#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const request = require('request');
const movieID = process.argv[2];
const getCharacters = new Promise((resolve, reject) => {
  request.get(
    `https://swapi-api.alx-tools.com/api/films/${movieID}/`,
    (err, response, body) => {
      if (!err) {
        try {
          resolve(JSON.parse(body).characters);
        } catch (error) {
          reject(error);
        }
      }
      reject(err);
    }
  );
});

getCharacters.then((characters) => {
  const charactersPromises = [];

  for (const character of characters) {
    charactersPromises.push(
      new Promise((resolve, reject) => {
        request.get(character, (err, response, body) => {
          if (err) reject(err);
          try {
            resolve(JSON.parse(body).name);
          } catch (error) {
            reject(error);
          }
        });
      })
    );
  }

  Promise.all(charactersPromises).then((names) => {
    for (const name of names) {
      console.log(name);
    }
  });
});
