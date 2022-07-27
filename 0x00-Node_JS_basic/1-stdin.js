const readline = require('readline');

const input = process.stdin;
const output = process.stdout;

console.log('Welcome to Holberton School, what is your name?');
const rlIn = readline.createInterface({ input, output })
  .on('line', (nm) => {
    console.log(`Your name is: ${nm}`);
    rlIn.close();
  })
  .on('close', () => console.log('This important software is now closing'));
