export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get length() {
    return this._length;
  }

  get name() {
    return this._name;
  }

  get students() {
    return this._students;
  }

  set length(val) {
    if (typeof val !== 'number') throw Error('length must be a Number');
    this._length = val;
  }

  set name(val) {
    if (typeof val !== 'string') throw Error('name must be a String');
    this._name = val;
  }

  set students(val) {
    if (!Array.isArray(val)) throw Error('students must be an Array');
    for (const st of val) {
      if (typeof st !== 'string') throw Error('students must contain Strings');
    }
    this._students = val;
  }
}
