export default function updateStudentGradeByCity(oList, city, newGrades) {
  return oList
    .filter((active) => active.location === city)
    .map((st) => {
      const g = newGrades.filter((g) => g.studentId === st.id);
      const grade = g.length ? g[0].grade : 'N/A';
      return { ...st, grade };
    });
}
