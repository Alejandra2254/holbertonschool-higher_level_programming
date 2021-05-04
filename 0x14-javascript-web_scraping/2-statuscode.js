#!/usr/bin/node
// function to read a file passing as argumment
const request = require('request');
const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log('code: %d', response.statusCode);
});
