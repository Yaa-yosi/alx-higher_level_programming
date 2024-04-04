#!/usr/bin/node

const arg = process.argv[2];
let i, j, row;

if (!arg || isNaN(arg)) console.log('Missing size');
else{
	if (arg > 0){
		for (i = 0; i < arg; i++){
			row = '';
			for (j = 0; j < arg; j++){
				row += 'X';
			}
		console.log(row);
		}
	}
}
