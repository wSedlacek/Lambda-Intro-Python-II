import { Entity } from './entity';
import { Item } from './item';

export class Room extends Entity {
  private _north: Room;
  private _south: Room;
  private _east: Room;
  private _west: Room;

  private _items: Item[];

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

  public northOf(room: Room) {
    room._north = this;
    this._south = room;
  }

  public southOf(room: Room) {
    room._south = this;
    this._north = room;
  }

  public eastOf(room: Room) {
    room._east = this;
    this._west = room;
  }

  public westOf(room: Room) {
    room._west = this;
    this._east = room;
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
}
