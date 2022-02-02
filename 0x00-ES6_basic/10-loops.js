export default function appendToEachArrayValue(array, appendString) {
  return array.map((idx) => appendString + idx);
}
