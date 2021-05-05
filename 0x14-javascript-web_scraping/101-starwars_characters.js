#!/usr/bin/node
// function to read a file passing as argumment
const num = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + num;
const request = require('request');
request(URL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    info.characters.forEach(function (element) {
      request(element, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const infoeach = JSON.parse(body);
          const name = infoeach.name;
          console.log(name);
        }
      });
    });
  }
});
