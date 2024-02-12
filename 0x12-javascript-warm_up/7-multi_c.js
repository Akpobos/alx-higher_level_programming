#!/usr/bin/node
if (isNaN(process.argv[2])) {
    return console.log('Missing number of occurrences');
}
for (let i = parseInt(process.argv[2]); i > 0; i--) {
    console.log('C is fun');
}
