#!/usr/bin/node
const { argv } = require('process');
let size;
if (!isNaN(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    size = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      size += 'X';
    }
    console.log(size);
  }
} else {
  console.log('Missing size');
}
