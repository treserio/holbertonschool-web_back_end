function calculateNumber(type, a, b) {
  if (typeof(type) != string) throw new TypeError('type not a string');
  if (isNaN(a) || isNaN(b)) throw new TypeError('NaN passed as argument');

  switch(type.toUpperCase()) {
    case 'SUM':
      return Math.round(a) + Math.round(b);
    case 'SUBTRACT':
      return Math.round(a) - Math.round(b);
    case 'DIVIDE':
      if (Math.round(b) === 0) return 'Error';
      return Math.round(a) / Math.round(b);
    default:
      throw TypeError(`type must be SUM, SUBTRACT or DIVIDE\nCurrently: ${type}`);
  }
}

module.exports = calculateNumber;
