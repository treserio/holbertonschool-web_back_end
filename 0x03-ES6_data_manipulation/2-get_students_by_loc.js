export default function getStudentsByLocation(oList, city) {
  return oList.filter(st => st.location === city);
}
