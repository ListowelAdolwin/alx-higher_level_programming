#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!(x)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
