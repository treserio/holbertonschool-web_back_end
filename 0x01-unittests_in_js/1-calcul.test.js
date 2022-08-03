const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
	describe('positives', () => {
    it('SUM', () => {
      assert.equal(calculateNumber('sum', 1, 3), 4);
      assert.equal(calculateNumber('sUm', 1, 3.7), 5);
      assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
      assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
      assert.equal(calculateNumber('SUM', 1.3, 0), 1);
    });

    it('SUBTRACT', () => {
      assert.equal(calculateNumber('subtract', 3, 1), 2);
      assert.equal(calculateNumber('sUbTrAcT', 3.7, 1), 3);
      assert.equal(calculateNumber('SUBTRACT', 3.7, 1.2), 3);
      assert.equal(calculateNumber('SUBTRACT', 3.7, 1.5), 2);
      assert.equal(calculateNumber('SUBTRACT', 1.3, 0), 1);
    });

    it('DIVIDE', () => {
      assert.equal(calculateNumber('divide', 4, 2), 2);
      assert.equal(calculateNumber('dIvIdE', 4.2, 2), 2);
      assert.equal(calculateNumber('DIVIDE', 5.5, 2.4), 3);
      assert.equal(calculateNumber('DIVIDE', 1.5, 3.7), 0.5);
    });
	});

  describe('negatives', () => {
    it('SUM', () => {
      assert.equal(calculateNumber('sum', -1, 3), 2);
      assert.equal(calculateNumber('sUm', -1, 3.7), 3);
      assert.equal(calculateNumber('SUM', -1.2, -3.7), -5);
      assert.equal(calculateNumber('SUM', 1.5, -3.7), -2);
      assert.equal(calculateNumber('SUM', -1.3, 0), -1);
    });

    it('SUBTRACT', () => {
      assert.equal(calculateNumber('subtract', -1, 3), -4);
      assert.equal(calculateNumber('sUbTrAcT', -1, 3.7), -5);
      assert.equal(calculateNumber('SUBTRACT', -1.2, -3.7), 3);
      assert.equal(calculateNumber('SUBTRACT', 1.5, -3.7), 6);
      assert.equal(calculateNumber('SUBTRACT', -1.3, 0), -1);
    });

    it('DIVIDE', () => {
      assert.equal(calculateNumber('divide', -4, -2), 2);
      assert.equal(calculateNumber('dIvIdE', -4.2, 2), -2);
      assert.equal(calculateNumber('DIVIDE', 5.5, -2.4), -3);
      assert.equal(calculateNumber('DIVIDE', -1.5, -3.7), 0.25);
    });
  });

  it('Errors', () => {
    assert.throws(() => calculateNumber(1, 'z'), TypeError);
    assert.throws(() => calculateNumber(NaN, 6.9), TypeError);
    assert.throws(() => calculateNumber(NaN, 6.9), TypeError);
    assert.equal(calculateNumber('DIVIDE', 1.3, 0), 'Error');
  });
})
