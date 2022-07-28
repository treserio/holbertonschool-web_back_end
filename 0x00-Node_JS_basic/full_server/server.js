// create a small Express server using the Router from ./routes/index
const exp = require('express');
const routes = require('./routes/index');

const app = exp();

app.use(routes)
  .listen(1245);

export default app;
