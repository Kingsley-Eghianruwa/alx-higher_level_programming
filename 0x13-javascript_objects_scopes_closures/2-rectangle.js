#!/usr/bin/node

class Rectangle {
  consructor () {}
}

module.exports = function rectangle (w, h) {
  const obj = new Rectangle();
  if (w > 0 && h > 0) {
    obj.width = w;
    obj.height = h;
  }
  return obj;
};
