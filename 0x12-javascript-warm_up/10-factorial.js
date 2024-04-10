#!/usr/bin/node

function fact (a) {
  if (a === 0 || a === 1) { return (1); } else { return (a * (fact(a - 1))); }
}

const a = parseInt(process.argv[2]);

if (!a) {
  console.log(1);
} else {
  console.log(fact(a));
}
