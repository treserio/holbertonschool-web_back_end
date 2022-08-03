const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
	describe('positives', () => {
    it('SUM', () => {
      expect(calculateNumber('sum', 1, 3)).to.equal(4);
      expect(calculateNumber('sUm', 1, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
      expect(calculateNumber('SUM', 1.3, 0)).to.equal(1);
    });

    it('SUBTRACT', () => {
      expect(calculateNumber('subtract', 3, 1)).to.equal(2);
      expect(calculateNumber('sUbTrAcT', 3.7, 1)).to.equal(3);
      expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
      expect(calculateNumber('SUBTRACT', 3.7, 1.5)).to.equal(2);
      expect(calculateNumber('SUBTRACT', 1.3, 0)).to.equal(1);
    });

    it('DIVIDE', () => {
      expect(calculateNumber('divide', 4, 2)).to.equal(2);
      expect(calculateNumber('dIvIdE', 4.2, 2)).to.equal(2);
      expect(calculateNumber('DIVIDE', 5.5, 2.4)).to.equal(3);
      expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.equal(0.5);
    });
	});

  describe('negatives', () => {
    it('SUM', () => {
      expect(calculateNumber('sum', -1, 3)).to.equal(2);
      expect(calculateNumber('sUm', -1, 3.7)).to.equal(3);
      expect(calculateNumber('SUM', -1.2, -3.7)).to.equal(-5);
      expect(calculateNumber('SUM', 1.5, -3.7)).to.equal(-2);
      expect(calculateNumber('SUM', -1.3, 0)).to.equal(-1);
    });

    it('SUBTRACT', () => {
      expect(calculateNumber('subtract', -1, 3)).to.equal(-4);
      expect(calculateNumber('sUbTrAcT', -1, 3.7)).to.equal(-5);
      expect(calculateNumber('SUBTRACT', -1.2, -3.7)).to.equal(3);
      expect(calculateNumber('SUBTRACT', 1.5, -3.7)).to.equal(6);
      expect(calculateNumber('SUBTRACT', -1.3, 0)).to.equal(-1);
    });

    it('DIVIDE', () => {
      expect(calculateNumber('divide', -4, -2)).to.equal(2);
      expect(calculateNumber('dIvIdE', -4.2, 2)).to.equal(-2);
      expect(calculateNumber('DIVIDE', 5.5, -2.4)).to.equal(-3);
      expect(calculateNumber('DIVIDE', -1.5, -3.7)).to.equal(0.25);
    });
  });

  it('Errors', () => {
    expect(() => calculateNumber(1, 'z')).to.throw(TypeError);
    expect(() => calculateNumber(NaN, 6.9)).to.throw(TypeError);
    expect(() => calculateNumber(NaN, 6.9)).to.throw(TypeError);
    expect(calculateNumber('DIVIDE', 1.3, 0)).to.equal('Error');
  });
})
