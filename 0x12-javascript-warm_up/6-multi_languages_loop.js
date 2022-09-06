#!/usr/bin/node

const strList = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const maxIdx = strList.length - 1;
let idx = 0;

while (idx <= maxIdx) {
  console.log(strList[idx]);
  idx = idx + 1;
}
