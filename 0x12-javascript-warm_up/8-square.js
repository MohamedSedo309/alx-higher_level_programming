#!/usr/bin/node
const x = process.argv[3];
const s = parseInt(x);
if (isNaN(s)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < s; i++) {
        console.log('X'.repeat(s));
    }
}
