// recreate task 5 using Express
const exp = require('express');
const countStudents = require('./3-read_file_async');

const app = exp();

app.get('/', (req, res) => res.send('Hello Holberton School!')).listen(1245);

app.get('/students', (req, res) => {
  let output = 'This is the list of our students\n';
  countStudents(process.argv[2])
    .then((data) => {
      output += `Number of students: ${data.total}\n`;
      for (const [k, v] of Object.entries(data.fields)) {
        output += `Number of students in ${k}: ${v.length}. List: ${v.join(', ')}`;
        // add new line to every entry except the last key
        if (k !== Object.keys(data.fields)[Object.keys(data.fields).length - 1]) {
          output += '\n';
        }
      }
      res.end(output);
    })
    .catch((err) => res.end(output + err.message));
}).listen(1245);

module.exports = app;
