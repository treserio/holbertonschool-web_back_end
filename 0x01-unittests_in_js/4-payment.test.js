const utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');


describe('sendPaymentRequestToApi', () => {
  it('sendPaymentRequestToAPI = calculateNumber', () => {
    const spiedFunction = sinon.spy(utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spiedFunction.calledWith('SUM', 100, 20)).to.be.true;
    spiedFunction.restore();
  });

  it('simulate a call to sendPaymentRequestToApi with stubs', () => {
    const stub = sinon.stub(utils, 'calculateNumber').returns(10);
    const spyFunction = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(spyFunction.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    spyFunction.restore();
  })
});
