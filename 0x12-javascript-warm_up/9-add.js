#!/usr/bin/node

function add (a, b) {
  const res = a + b;
  console.log(res);
}

const num1 = Math.floor(Number(process.argv?.[2]));
const num2 = Math.floor(Number(process.argv?.[3]));

add(num1, num2);
