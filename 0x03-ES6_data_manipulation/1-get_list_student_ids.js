export default function getListStudentIds(oList) {
  try {
    return oList.map((st) => st.id);
  } catch (e) {
    return [];
  }
}
