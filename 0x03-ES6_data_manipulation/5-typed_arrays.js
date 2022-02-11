export default function createInt8TypedArray(length, position, value) {
  if (position > length) throw Error('Position outside range');
  const buff = new ArrayBuffer(length);
  new Int8Array(buff)[position] = value;
  return new DataView(buff, 0);
}
