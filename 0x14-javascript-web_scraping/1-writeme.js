#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];
const string = process.argv[3];

try {
  fs.writeFileSync(filepath, string, 'utf-8');
} catch (error) {
  console.log(error);
}
