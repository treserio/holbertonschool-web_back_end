const utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');


describe('sendPaymentRequestToApi', () => {
  var spyFunction;

  beforeEach(() => {
    spyFunction = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyFunction.restore();
  });

  it('sendPaymentRequestToApi: 120', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyFunction.calledWith('The total is: 120')).to.be.true;
    expect(spyFunction.calledOnce).to.be.true;
  });

  it('sendPaymentRequestToApi: 20', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spyFunction.calledWith('The total is: 20')).to.be.true;
    expect(spyFunction.calledOnce).to.be.true;
  });
});
