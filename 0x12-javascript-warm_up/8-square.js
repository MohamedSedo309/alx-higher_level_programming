#!/usr/bin/node
const s = process.argv[3];
if (isNaN(s)) {
    print('Missing size');
} else {
    for (let i = 0; i < s; i++) {
        print('X'.repeat(s));
    }
}
