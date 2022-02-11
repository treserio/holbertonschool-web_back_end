export default function createInt8TypedArray(length, position, value) {
  try {
    const buff = new ArrayBuffer(length);
    new Int8Array(buff)[position] = value;
    return buff;
  } catch (e) {
    throw Error('Position outside range');
  }
}
