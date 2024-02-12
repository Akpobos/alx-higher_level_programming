#!/usr/bin/node
const args = process.argv;
const first = args[2];
if (first) {
    console.log(first);
} else {
    console.log('No argument');
}
