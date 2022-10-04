#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor(w, h) {
  if ((w = parseInt(w)) < 0 || (h = parseInt(h)) < 0) {
    this.width = w;
    this.height = h;
    }
  }
 
  print() {
    let i = 0;
    let j = 0;
    for(i = 0; i < this.width; i++) {
      for(j = 0; j < this.h; j++) {
        console.log('X');
      }
    }

  }
}

module.exports = Rectangle;
