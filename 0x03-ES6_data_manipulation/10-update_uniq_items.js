export default function updateUniqueItems(inMap) {
  if (!(inMap instanceof Map)) throw Error('Cannot Process');
  inMap.forEach((v, k) => {
    if (v === 1) inMap.set(k, 100);
  });
}
