#!/usr/bin/node
// function to read a file passing as argumment
var request = require('request');
const url_r = process.argv[2];

request.get(url_r).on('response', function (response) {
  console.log('code: %d', response.statusCode);
});