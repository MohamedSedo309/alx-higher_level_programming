#!/usr/bin/node
const argu = process.argv.slice(2);
if (argu.length === 0) { console.log('No argument'); } else if (argu.length === 1) { console.log('Argument found'); } else { console.log('Arguments found'); }
