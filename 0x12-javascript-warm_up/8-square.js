#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < parseInt(size); i++) {
        let sq = '';
        for (let j = 0; j < parseInt(size); j++) {
            sq += 'X';
        }
        console.log(sq);
    }
}
