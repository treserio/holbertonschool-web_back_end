export default function cleanSet(set, startString) {
  if (!set || !startString || typeof startString !== 'string') return '';

  return Array.from(set)
    .map((val) => {
      if (typeof val === 'string' && val.startsWith(startString)) {
        return val.replace(startString, '');
      }
      return undefined;
    })
    .filter((val) => val)
    .join('-');
}
