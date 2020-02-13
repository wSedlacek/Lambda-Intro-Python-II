import { Entity, Item } from '../..';

export class Room extends Entity {
  private _north: Room;
  private _south: Room;
  private _east: Room;
  private _west: Room;

  private readonly _items: Item[];

  constructor(name: string, description: string, items: Item[] = []) {
    super(name, description);
    this._items = items;
  }

  public toString() {
    let details = `===${this.name}===
${this.description}\n`;

    for (const item of this.items) {
      details += item.toString();
    }

    details += '\n';
    return details;
  }

  public set north(room: Room) {
    room._north = this;
    this._south = room;
  }

  public set south(room: Room) {
    room._south = this;
    this._north = room;
  }

  public set east(room: Room) {
    room._east = this;
    this._west = room;
  }

  public set west(room: Room) {
    room._west = this;
    this._east = room;
  }

  public get north() {
    return this._north;
  }

  public get south() {
    return this._south;
  }

  public get east() {
    return this._east;
  }

  public get west() {
    return this._west;
  }

  public get items() {
    return this._items;
  }

  public take(index: number) {
    return this._items.splice(index, 1);
  }

  public drop(item: Item) {
    this._items.push(item);
  }
}
