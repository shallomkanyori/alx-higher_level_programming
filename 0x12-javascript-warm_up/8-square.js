#!/usr/bin/node

const num1 = Number(process.argv?.[2]);

if (!num1) {
  console.log('Missing size');
} else {
  const size = Math.floor(num1);

  for (let r = 0; r < size; r++) {
    let row = '';

    for (let c = 0; c < size; c++) {
      row += 'X';
    }

    console.log(row);
  }
}
