#!/usr/bin/node
// function to read a file passing as argumment
const file = process.argv[2];
const data = process.argv[3];
const fs = require('fs');
fs.writeFile(file, data, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
