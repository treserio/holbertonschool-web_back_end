// a more complex http server
const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');

    countStudents(process.argv[2])
      .then((data) => {
        res.write(`Number of students: ${data.total}\n`);
        for (const [k, v] of Object.entries(data.fields)) {
          res.write(`Number of students in ${k}: ${v.length}. List: ${v.join(', ')}`);
          // add new line to every entry except the last key
          if (k !== Object.keys(data.fields)[Object.keys(data.fields).length - 1]) {
            res.write('\n');
          }
        }
        res.end();
      })
      .catch((err) => res.end(err));
  }
})
  .listen(1245);

module.exports = app;
