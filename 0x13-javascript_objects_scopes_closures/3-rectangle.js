#!/usr/bin/node

class Rectangle {
  consructor () {}
}

const rectangleMethods = {
  print () {
    let idx = 1;
    let idy = 1;
    const xhar = 'X';
    let recWidth = '';
    while (idx <= this.width) {
      recWidth = recWidth.concat(xhar);
      idx = idx + 1;
    }
    while (idy <= this.height) {
      console.log(recWidth);
      idy = idy + 1;
    }
  }
};

module.exports = function rectangle (w, h) {
  const obj = new Rectangle();
  if (w > 0 && h > 0) {
    obj.width = w;
    obj.height = h;
  }
  obj.print = rectangleMethods.print;
  return obj;
};
