export default function appendToEachArrayValue(array, appendString) {
  let i = 0;
  for (var idx of array) {
    array[i] = appendString + idx;
    i += 1;
  }

  return array;
}
