#!/usr/bin/node
// function to read a file passing as argumment
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body);
    const stats = {};
    for (const x in results) {
      const data = results[x];
      if (data.completed === true) { // separes dicts where completed is true
        const id = data.userId;
        if (id in stats) { // check if id exist on the dic, if exist add 1
          stats[id] += 1;
        } else {
          stats[id] = 1; // if no exist, created with value 1
        }
      }
    }
    console.log(stats);
  }
});
