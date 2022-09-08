#!/usr/bin/node

function rfact (idx, result) {
  if (idx === 1 || idx === 0) {
    return result;
  }
  result = result * idx;
  idx = idx - 1;

  return rfact(idx, result);
}

function fact (n) {
  const result = 1;
  const idx = n;
  return rfact(idx, result);
}

const value = Number(process.argv[2]);

if (isNaN(value)) {
  console.log(1);
} else {
  const output = fact(value);
  console.log(output);
}
