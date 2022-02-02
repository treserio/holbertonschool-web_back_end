export default function appendToEachArrayValue(array, appendString) {
  const eat = [];
  for (const aDonk of array) {
    eat.push(appendString + aDonk);
  }

  return eat;
}
