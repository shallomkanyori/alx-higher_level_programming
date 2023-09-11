#!/usr/bin/node

const num1 = Number(process.argv?.[2]);

if (!num1) {
  console.log('Missing number of occurrences');
} else {
  const x = Math.floor(num1);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
