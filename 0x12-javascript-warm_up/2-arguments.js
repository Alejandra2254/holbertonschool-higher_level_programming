#!/usr/bin/node
// Write a script that prints 3 lines
const process = require('process');
let args = process.argv;
if (args.length === 2)
    console.log('No argument');
if (args.length === 3)
    console.log('Argument found');
if (args.length > 3)
    console.log('Arguments found');
