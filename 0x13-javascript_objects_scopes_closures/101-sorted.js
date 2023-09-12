#!/usr/bin/node

const dict = require('./101-data').dict;
const res = {};

for (const userId in dict) {
  const occs = dict[userId].toString();

  if (!res[occs]) {
    res[occs] = [];
  }

  res[occs].push(userId);
}

console.log(res);
