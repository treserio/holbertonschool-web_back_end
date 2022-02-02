export default function createIteratorObject(report) {
  const iterator = {
    dep: 0,
    emp: 0,
    report: report.allEmployees,
    next() {
      // store keys from the report
      const keys = Object.keys(this.report);
      // check that the allEmployee dictionary has a key
      if (keys[this.dep]) {
        // if this.emp exists, iterate the employee for the next next()
        if (this.report[keys[this.dep]][this.emp]) {
          this.emp += 1;
          return {
            // returning the the employee name at this.emp indx - 1 since we've moved passed it
            value: this.report[keys[this.dep]][this.emp - 1],
            done: false,
          };
        }
        this.dep += 1;
        this.emp = 0;
        return this.next();
      }
      return { value: null, done: true };
    },
    [Symbol.iterator]() {
      return this;
    },
  };
  return iterator;
}
