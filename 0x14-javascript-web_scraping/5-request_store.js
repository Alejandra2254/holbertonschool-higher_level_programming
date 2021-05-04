#!/usr/bin/node
// function to read a file passing as argumment
const file = process.argv[3];
const URL = process.argv[2];
const fs = require('fs');
const request = require('request');
request(URL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const content = body;
    fs.writeFile(file, content, 'utf-8', function (err) {
        if (err) {
          return console.log(err);
        }
      });
  }
});
