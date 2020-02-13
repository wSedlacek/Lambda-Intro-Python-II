import { Entity, Item, Room } from '../..';

export class Player extends Entity {
  private _room: Room;
  private readonly _items: Item[];

  constructor(name: string, room: Room) {
    super(name, 'PC');
    this._room = room;
    this._items = [];
  }

  public toString() {
    let details = `===${this.name}===\n`;

    for (const item of this._items) {
      details += item.toString();
    }

    details += '\n';
    return details;
  }

  public move(direction: 'n' | 'north' | 's' | 'south' | 'e' | 'east' | 'w' | 'west') {
    if (direction === 'n') direction = 'north';
    if (direction === 's') direction = 'south';
    if (direction === 'e') direction = 'east';
    if (direction === 'w') direction = 'west';

    let room = this.room[direction];
    if (!room) throw new Error('INVALID ROOM!');
    this._room = room;
  }

  public take(itemName: string) {
    const index = this._room.items.findIndex((item) => item.hasName(itemName));
    if (index === -1) throw new Error('INVALID ITEM!');
    const [item] = this._room.take(index);
    this._items.push(item);
    item.onTake();
  }

  public drop(itemName: string) {
    const index = this._items.findIndex((item) => item.hasName(itemName));
    if (index === -1) throw new Error('INVALID ITEM!');
    const [item] = this._items.splice(index, 1);
    this._room.drop(item);
    item.onDrop();
  }

  public get room() {
    return this._room;
  }

  public get north() {
    return this._room.north;
  }

  public get south() {
    return this._room.south;
  }

  public get east() {
    return this._room.east;
  }

  public get west() {
    return this._room.west;
  }

  public get items() {
    return this._items.length > 0 ? this._items : null;
  }
}
