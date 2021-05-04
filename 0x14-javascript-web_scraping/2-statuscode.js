#!/usr/bin/node
// function to read a file passing as argumment
var request = require('request');
const url_r = process.argv[2];

request(url_r, function (error, response, body) {
  if (error) console.error('error:', error); // Print the error if one occurred
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
