#!/usr/bin/node
// concat a sentence
const count = process.argv;
const number = parseInt(count[2]);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
