#!/usr/bin/node
// print process.argv
const count = process.argv;
if (count[2]) {
  console.log(count[2]);
} else {
    console.log("No argument")
}
