// controller for returning on /students route
const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    let output = 'This is the list of our students\n';
    readDatabase(process.argv[2])
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
  }

  static getAllStudentsByMajor(req, res) {
    readDatabase(process.argv[2])
      .then((data) => {
        console.log('req params:', req.params.major);
        if (req.params.major && !req.params.major in ['CS', 'SWE']) {
          res.status(500).end('Major parameter must be CS or SWE');
        }
        for (const [k, v] of Object.entries(data.fields)) {
          if (req.params.major == k) res.end(`List: ${v.join(', ')}`);
        }
      })
      .catch((err) => res.end(err.message));
  }
}

