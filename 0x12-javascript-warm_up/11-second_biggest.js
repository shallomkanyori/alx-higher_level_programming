#!/usr/bin/node

const args = process.argv;
const nums = [];

for (let i = 2; i < args.length; i++) {
  nums.push(Math.floor(Number(args[i])));
}

if (nums.length <= 1) {
  console.log('0');
} else {
  let max = -Infinity;
  let max2 = max;

  for (const n of nums) {
    if (n > max) {
      max2 = max;
      max = n;
    } else if (n > max2) {
      max2 = n;
    }
  }

  console.log(max2);
}
