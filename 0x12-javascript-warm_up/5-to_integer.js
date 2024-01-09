#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) { console.log('Not a number'); } else { console.log(x); }
