#!/usr/bin/node

const argList = process.argv;
const firstArg = argList[2];
const isFirstArg = typeof (argList[2]);

if (isFirstArg === 'undefined') {
  console.log('No argument');
} else {
  console.log(firstArg);
}
