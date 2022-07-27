const readline = require('readline');
const proc = require('process');

input = proc.stdin;
output = proc.stdout;

console.log('Welcome to Holberton School, what is your name?');
interface = readline.createInterface({input, output})
  .on('line', (nm) => {
    console.log(`Your name is: ${nm}`);
    interface.close();
  })
  .on('close', () => console.log('This important software is now closing'));
