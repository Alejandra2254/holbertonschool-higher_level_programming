#!/usr/bin/node
// Write a script that prints a square
const size = parseInt(process.argv[2]);
let i = 0; let j = 0;
if (Number.isNaN(size)) {
  console.log('Missing size');
}
while (i < size) {
  while (j < size) {
    console.log('X'.repeat(size));
    j++;
  }
  i++;
}
