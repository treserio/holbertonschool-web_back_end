export default function getStudentIdsSum(oList) {
  return oList.reduce((val, st) => val + st.id, 0);
}
