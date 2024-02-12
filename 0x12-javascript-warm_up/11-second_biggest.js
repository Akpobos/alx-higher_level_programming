#!/usr/bin/node
let index = 0;
const arr = [];
for (const a of process.argv) {
  if (index >= 2) {
    arr.push(a);
  }
  index++;
}
console.log(arr.length > 1 ? arr.sort((a, b) => b - a)[1] : 0);