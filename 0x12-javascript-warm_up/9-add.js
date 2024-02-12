#!/usr/bin/node
const arg = process.argv;
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(arg[2], arg[3]);
