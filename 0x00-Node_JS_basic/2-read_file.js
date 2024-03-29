// syncronous read of a file and appropriate print
const fs = require('fs');

module.exports = function countStudents(file) {
  let fullList = [];
  try {
    fullList = fs.readFileSync(file, 'utf8').split('\n').slice(1);
  } catch (e) {
    throw Error('Cannot load the database');
  }
  const students = fullList.filter((st) => st !== '');
  // setup obj with our fields and their student lists
  const fields = {};
  students.forEach((st) => {
    if (!fields[st.split(',')[3]]) fields[st.split(',')[3]] = [];
    fields[st.split(',')[3]].push(st.split(',')[0]);
  });
  // print required messages
  console.log(`Number of students: ${students.length}`);
  for (const [k, v] of Object.entries(fields)) {
    console.log(`Number of students in ${k}: ${v.length}. List: ${v.join(', ')}`);
  }
};
