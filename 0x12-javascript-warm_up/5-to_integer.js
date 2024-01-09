#!/usr/bin/node
const y = process.argv[2];
const x = parseInt(y);
if (isNaN(x)) { console.log('Not a number'); } else { console.log(x); }
