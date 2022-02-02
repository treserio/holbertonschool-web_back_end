export default function createIteratorObject(report) {
  const iterator = {
    step: 0,
    dep: 0,
    report: report.allEmployees,
    next() {
      if (Object.keys(this.report)[this.dep]) {
        this.step += 1;
        if (this.report[Object.keys(this.report)[this.dep]][this.step - 1]) {
          return {
            value: this.report[Object.keys(this.report)[this.dep]][this.step - 1],
            done: false,
          };
        }
        this.dep += 1;
        this.step = 0;
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
