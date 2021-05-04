#!/usr/bin/node
// function to read a file passing as argumment
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const x in results) {
      const characters = results[x].characters;
      for (const y in characters) {
        if (characters[y].search('/18/') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});