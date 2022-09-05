#!/usr/bin/node

const cmdLineArg = process.argv;
const numOfArg = cmdLineArg.length - 2;

if (numOfArg === 0) {
  console.log('No argument');
} else if (numOfArg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
