#!/usr/bin/node

/*
 * if no argument print "No arugment"
 * if 1 argument print "Argument found"
 * if >=2 or >1 argument print "Arguments found"
 */

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
