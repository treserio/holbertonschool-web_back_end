// execute through the command line
console.log('Welcome to Holberton School, what is your name?');
process.stdin
  .on('readable', () => {
    const nm = process.stdin.read();
    nm && process.stdout.write(`Your name is: ${nm}`);
  })
  .on('end', () => console.log('This important software is now closing'));
