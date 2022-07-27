// create a small HTTP server using Express module
const exp = require('express');

const app = exp();

app.get('/', (req, res) => res.send('Hello Holberton School!')).listen(1245);

module.exports = app;
