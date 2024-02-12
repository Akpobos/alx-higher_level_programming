#!/usr/bin/node
const args = process.argv.length;
console.log(args <= 2 ? 'No argument' : `Argument${args > 3 ? 's' : ''} found`);
