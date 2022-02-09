export default class Currency {
  constructor(cd, nm) {
    this.code = cd;
    this.name = nm;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(val) {
    this._code = val;
  }

  set name(val) {
    this._name = val;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
