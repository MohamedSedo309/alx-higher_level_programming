#!/usr/bin/node
const arg = process.argv[2];
num = parseInt(arg);
if (isNaN(num)) {
    console.log('Missing size')
} else {
    for (i = 0; i < num; i++) {
        for (i = 0; i < num; i++) {
            console.log('X'.repeat(num))
        }
    }
}
