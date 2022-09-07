#!/usr/bin/node

const numOfArg = process.argv.length - 2;

if (numOfArg < 2) {
  console.log(0);
} else {
  let largesetNum = 0;
  let secondLargestNum = 0;
  let idx = 0;
  const argArray = process.argv.slice(2);
  console.log(argArray);

  while (idx < argArray.length) {
    if (Number(argArray[idx]) > largesetNum) {
      secondLargestNum = largesetNum;
      largesetNum = Number(argArray[idx]);
    } else if (Number(argArray[idx]) > secondLargestNum) {
      secondLargestNum = Number(argArray[idx]);
    } else {
      // do nothing
    }
    idx = idx + 1;
  }
  console.log(secondLargestNum);
}
