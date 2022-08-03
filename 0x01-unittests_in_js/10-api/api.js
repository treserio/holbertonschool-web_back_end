const express = require('express');
const app = express();

app
  .get('/', (req, res) => {
    res.send('Welcome to the payment system');
  })
  .get('/cart/:id([0-9]*)', (req, res) => {
    res.send(`Payment methods for cart ${req.params.id}`);
  })
  .get('/available_payments', (req, res) => {
    res.json({
      payment_methods: {
        credit_cards: true,
        paypal: false
      }
    });
  })
  .use(express.json()).post('/login', (req, res) => {
    res.send(`Welcome ${req.body.userName}`);
  })
  .listen(7865, () => {
    console.log('API available on localhost port 7865');
  });

module.exports = app;
