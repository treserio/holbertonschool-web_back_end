export default function getListStudentIds(oList) {
  try {
    return oList.map((val) => val.id);
  } catch (e) {
    return [];
  }
}
