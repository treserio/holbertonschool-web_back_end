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
});
