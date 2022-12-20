#!/usr/bin/node
/*
 * A script that prints first argument
 * if 0 argument print "No argument"
 */

if (process.argv[2] === undefined) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
