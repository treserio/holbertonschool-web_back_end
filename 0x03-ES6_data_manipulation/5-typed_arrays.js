export default function createInt8TypedArray(length, position, value) {
  try {
    const abuff = new Int8Array(length);
    abuff[position] = value;
    return abuff;
  } catch (e) {
    throw Error('Position outside range');
  }
}
