#!/usr/bin/node

const argList = process.argv;
const firstArg = argList[2];
const isFirstArg = typeof (argList[2]);

if (isFirstArg === 'undefined') {
  console.log('No arguments');
} else {
  console.log(firstArg);
}
