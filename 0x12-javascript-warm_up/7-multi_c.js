#!/usr/bin/node

const arg = process.argv[2];
let i;

if (!arg) console.log('Missing number of occurrences');
else{
	for (i = 0; i < arg; i++) console.log('C is fun');
}
