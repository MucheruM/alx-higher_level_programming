#!/usr/bin/node

const x = parseInt(process.argv[2]);
let counter = 0;

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  while (counter < x) {
    console.log('C is fun');
    counter++;
  }
}
