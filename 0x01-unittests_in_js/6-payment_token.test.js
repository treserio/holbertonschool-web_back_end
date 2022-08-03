const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');


describe('getPaymentTokenFromAPI', () => {
  it('confirm promise', (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      expect(response.data).to.equal('Successful response from the API');
      done();
    });
  });
});
