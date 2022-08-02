function calculateNumber(a, b) {
  // if (isNaN(a) || isNaN(b)) throw TypeError('NaN was passed');
	return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
