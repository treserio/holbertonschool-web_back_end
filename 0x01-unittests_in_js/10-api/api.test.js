const expect = require('chai').expect;
const request = require('request');

describe('API Test', () => {
  it('Tests that GET returns correct code and results', (done) => {
    request('http://localhost:7865/', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Tests /cart/:id is working', (done) => {
    request('http://localhost:7865/cart/1', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 1');
      done();
    });
  });

  it('Tests /cart/:id fails when given non-number', (done) => {
    request('http://localhost:7865/cart/a', (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('Tests /available_payments returns correctly', (done) => {
    request(
      'http://localhost:7865/available_payments',
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal(
          '{"payment_methods":{"credit_cards":true,"paypal":false}}'
        );
        done();
      }
    );
  });

  it('Tests POST /login returns correctly', (done) => {
    request({
        method: 'POST',
        uri: 'http://localhost:7865/login',
        json: {
          userName: 'John'
        }
      },
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome John');
        done();
      }
    );
  });
});
