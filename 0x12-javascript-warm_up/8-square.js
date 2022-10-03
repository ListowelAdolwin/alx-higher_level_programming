#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!(x)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < x) {
    let j = 0;
    let sides = '';
    while (j < x) {
      sides += 'X';
      j++;
    }
    console.log(sides);
    i++;
  }
}
