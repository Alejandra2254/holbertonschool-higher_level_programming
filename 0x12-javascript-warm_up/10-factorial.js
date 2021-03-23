#!/usr/bin/node
// Write a script that prints a square
const number = parseInt(process.argv[2]);

if (Number.isNaN(number) || number === 0 || number === 1) {
  console.log(parseInt('1'));
} else {
  console.log(factorial(number));
}
function factorial (n) {
  if (n > 1) {
    return n * factorial(n - 1);
  }
  return 1;
}
