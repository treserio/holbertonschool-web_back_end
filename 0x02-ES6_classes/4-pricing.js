/* eslint-disable no-unused-vars */
import Currency from './3-currency';

export default class Pricing {
  constructor(amnt, curr) {
    this.amount = amnt;
    this.currency = curr;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(amnt) {
    this._amount = amnt;
  }

  set currency(curr) {
    this._currency = curr;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
