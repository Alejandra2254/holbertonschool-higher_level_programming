#!/usr/bin/node
// function to read a file passing as argumment
const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(`${args[0]}`, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
