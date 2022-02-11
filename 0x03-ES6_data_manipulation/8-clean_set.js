export default function cleanSet(set, startString) {
  try {
    return Array.from(set)
      .map((val) => {
        if (startString && val.startsWith(startString)) {
          return val.replace(startString, '');
        }
      })
      .filter((val) => val)
      .join('-');
  } catch (e) {
    return '';
  }
}
