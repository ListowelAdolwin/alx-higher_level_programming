#!/usr/bin/node
exports.multipleCalls = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
