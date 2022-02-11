export default function updateUniqueItems(inMap) {
  if (!(inMap instanceof Map)) throw Error('Cannot Process');
  const oMap = new Map();
  inMap.forEach((v, k) => {
    if (v === 1) {
      oMap.set(k, 100);
    } else {
      oMap.set(k, v);
    }
  });
  return oMap;
}
