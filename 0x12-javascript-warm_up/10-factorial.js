#!/usr/bin/node
const firstNum = parseInt(process.argv[2]);

function factorial (firstNum) {
  if (isNaN(firstNum) || firstNum === 0) {
    return (1);
  } else if (firstNum < 0) {
    return (-1);
  } else {
    return (firstNum * factorial(firstNum - 1));
  }
}

console.log(factorial(firstNum));
