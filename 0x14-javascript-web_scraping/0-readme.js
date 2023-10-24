#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];

try {
  const text = fs.readFileSync(filepath, 'utf-8');
  console.log(text);
} catch (error) {
  console.log(error);
}
