#!/usr/bin/node
'use strict';

function getSecondLargest (array) {
  return (array.length > 1) ? array.sort((a, b) => b - a)[1] : 0;
}

function convertToIntegerArray (array) {
  return array.map((num) => parseInt(num));
}

const array = convertToIntegerArray(process.argv.slice(2));

console.log(getSecondLargest(array));
