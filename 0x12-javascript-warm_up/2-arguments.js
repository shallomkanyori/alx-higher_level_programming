#!/usr/bin/node

const argLen = process.argv.length - 2;

if (argLen > 1) {
  console.log('Arguments found');
} else if (argLen > 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
