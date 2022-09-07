#!/usr/bin/node

function add (a, b) {
  let result = 0;
  result = a + b;
  return result;
}

const op1 = Number(process.argv[2]);
const op2 = Number(process.argv[3]);
let output = 0;

if (isNaN(op1) || isNaN(op2)) {
  output = NaN;
} else {
  output = add(op1, op2);
}

console.log(output);
