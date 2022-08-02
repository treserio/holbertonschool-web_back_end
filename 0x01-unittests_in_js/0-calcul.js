// calculateNumber takes 2 numbers and return the sum of their rounded values

function calculateNumber(a, b) {
  if (isNaN(a) || isNaN(b)) throw new TypeError("NaN passed as argument");
	return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
