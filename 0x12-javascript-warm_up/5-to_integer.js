#!/usr/bin/node
const { argv } = require('process');
console.log(isNaN(argv[2]) ? 'Not a number' : `My number: ${argv[2]}`);
