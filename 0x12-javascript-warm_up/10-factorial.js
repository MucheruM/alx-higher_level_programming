#!/usr/bin/node
'use strict';

function factorial (n) {
    if (!n) {
	return 1;
    }

    return n * factorial(n - 1);
}

const n = parseInt(process.argv[2], 10);
console.log(factorial(n));
