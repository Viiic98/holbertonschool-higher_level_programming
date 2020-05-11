#!/usr/bin/node
const Sq = require('./5-square.js');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.width; x++) {
        let row = '';
        for (let y = 0; y < this.height; y++) {
          row += c;
        }
        console.log(row);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
