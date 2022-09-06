#!/usr/bin/node

const count = Number(process.argv[2]);
let idx = 1;

if (isNaN(count) || count === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (idx <= count) {
    console.log('C is fun');
    idx = idx + 1;
  }
}
