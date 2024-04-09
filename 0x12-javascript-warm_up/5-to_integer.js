#!/usr/bin/node

const num = parseInt(process.argv[2]);

console.log((num) ? `My number: ${num}` : 'Not a number');

// if (!isNaN(num)) console.log('My number: ' + num);
// else console.log('Not a number');
