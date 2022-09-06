#!/usr/bin/node

const argValue = process.argv[2];
let result = Number(argValue);

if (isNaN(result) || result === undefined) {
  console.log('Not a number');
} else {
  result = ~~result;
  console.log('My number: ' + result);
}
