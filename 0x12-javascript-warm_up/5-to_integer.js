#!/usr/bin/node

const arg1 = process.argv?.[2];
const num1 = Number(arg1);

if (num1) {
  console.log(`My number: ${Math.floor(num1)}`);
} else {
  console.log('Not a number');
}
