#!/usr/bin/node

const num = process.argv[2];

if (!num || isNaN(num)) console.log('Not a number');
else console.log(num);
