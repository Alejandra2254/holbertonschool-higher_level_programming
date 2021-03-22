#!/usr/bin/node
// Write a script that prints 3 lines
const count = process.argv.length;
if (count === 3)
    console.log('Argument found');
else if (count > 3)
    console.log('Arguments found');
else
    console.log('No argument')
