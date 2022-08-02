const assert = require('assert')
const calculateNumber = require('./0-calcul')

describe('calculateNumber', () => {
	it('positives', () => {
		assert.equal(calculateNumber(1, 3), 4);
		assert.equal(calculateNumber(1, 3.7), 5);
		assert.equal(calculateNumber(1.2, 3.7), 5);
		assert.equal(calculateNumber(1.5, 3.7), 6);
		assert.equal(calculateNumber(1.3, 0), 1);
	});

	it('negatives', () => {
		assert.equal(calculateNumber(-1, 3), 2);
		assert.equal(calculateNumber(-1, 3.7), 3);
		assert.equal(calculateNumber(-1.2, -3.7), -5);
		assert.equal(calculateNumber(1.5, -3.7), -2);
		assert.equal(calculateNumber(-1.3, 0), -1);
	});

  it('NaN', () => {
    assert.throws(() => calculateNumber(1, 'z'), TypeError);
    assert.throws(() => calculateNumber(NaN, 6.9), TypeError);
  });
})
