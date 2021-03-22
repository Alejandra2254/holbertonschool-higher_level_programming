#!/usr/bin/node
// print process.argv
const count = process.argv;
if (count[2]) {
  if (count[3]) {
    console.log(count[2] + ' is ' + count[3]);
  } else {
    console.log(count[2] + ' is undefined');
  }
} else {
  console.log('undefined is undefined');
}
