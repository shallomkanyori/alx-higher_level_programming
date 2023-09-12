#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';

      for (let j = 0; j < this.width; j++) {
        row += c;
      }

      console.log(row);
    }
  }
}

module.exports = Square;
