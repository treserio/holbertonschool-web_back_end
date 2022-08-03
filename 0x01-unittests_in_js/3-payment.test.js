const utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');


describe('sendPaymentRequestToApi', () => {
  it('sendPaymentRequestToAPI = calculateNumber', () => {
    const spiedFunction = sinon.spy(utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spiedFunction.calledWith('SUM', 100, 20)).to.be.true;
    spiedFunction.restore();
  });
});
