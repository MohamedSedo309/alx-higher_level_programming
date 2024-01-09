#!/usr/bin/node
const x = process.argv[2];
if (x === undefined) {
    console.log('Missing number of occurrences');
} else {
    for (let i=0; i < 5; i++){
        console.log('C is fun')
    }
}
