#!/usr/bin/node
const parsable = parseInt(process.argv[2]);
if (!(parsable)) {
  console.log('Not a number');
} else {
  console.log('My number: ', (parsable));
}
