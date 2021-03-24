#!/usr/bin/node
const array = require('./100-data.js').list;
const out = array.map((x, index) => x * index);
console.log(array);
console.log(out);
