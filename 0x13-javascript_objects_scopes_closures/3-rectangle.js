#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if ((width > 0 && height > 0)) {
      this.width = width;
      this.height = height;
    }
  }

  /**
   * Print a rectangle using 'X'
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdouwrit('X');
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Rectangle;
