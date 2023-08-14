#!/usr/bin/node
const arg = process.argv[2];
num = parseInt(arg);
if (isNaN(num)) { console.log('Missing number of occurrences') } else { for (i = 0; i < num; i++) { console.log('C is fun') } }
