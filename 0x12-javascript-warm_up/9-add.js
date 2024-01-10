#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0]);
const y = parseInt(args[1]);
if (isNaN(x) || isNaN(y)) {
  console.log('NaN');
} else {
  console.log(add(x, y));
}
function add (a, b) {
  return a + b;
}
