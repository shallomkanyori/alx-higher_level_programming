#!/usr/bin/node

const fs = require('fs');

const args = process.argv;
const file1 = args?.[2];
const file2 = args?.[3];
const dest = args?.[4];

if (!file1 || !file2 || !dest) {
  console.log('Usage: ./102-concat.js src1 src2 dest');
} else {
  try {
    const data1 = fs.readFileSync(file1).toString();
    const data2 = fs.readFileSync(file2).toString();
    const input = data1 + data2;

    fs.writeFileSync(dest, input, 'utf-8');
  } catch (err) {
    console.error(`Error concatenating files: ${err.message}`);
  }
}
