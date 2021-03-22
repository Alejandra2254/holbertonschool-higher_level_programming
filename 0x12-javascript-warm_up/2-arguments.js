#!/usr/bin/node
// Write a script that prints 3 lines
const count = process.argv.length;
if (count === 2) {
    console.log('No argument');
} else if (count === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');   
}
