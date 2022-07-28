// create a function named readDatabase that accepts a file path read the database asynchronously
const countStudents = require('../3-read_file_async');

function readDatabase(path) { countStudents(path); }

module.exports = readDatabase;
