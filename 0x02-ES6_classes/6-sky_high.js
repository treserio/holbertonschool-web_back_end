import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, flrs) {
    super(sqft);
    this._floors = flrs;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
