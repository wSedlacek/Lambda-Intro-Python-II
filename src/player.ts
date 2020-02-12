import { Entity } from './entity';
import { Item } from './item';
import { Room } from './room';

export class Player extends Entity {
  private currentRoom: Room;
  private items: Item[];

  constructor(name: string, room: Room) {
    super(name, 'PC');
    this.currentRoom = room;
    this.items = [];
  }

  public toString() {
    let details = `===${this.name}===\n`;

    for (const item of this.items) {
      details += item.toString();
    }

    details += '\n';
    return details;
  }

  public look() {
    return this.currentRoom;
  }

  public move(room: Room) {
    this.currentRoom = room;
  }

  public take(itemName: string) {
    const item = this.currentRoom.items.find((item) => item.hasName(itemName));
    if (item === undefined) throw new Error('INVALID ITEM!');
    this.currentRoom.take(item);
    this.items.push(item);
    item.onTake();
  }

  public drop(itemName: string) {
    const index = this.items.findIndex((item) => item.hasName(itemName));
    if (index === -1) throw new Error('INVALID ITEM!');
    const [item] = this.items.splice(index, 1);
    this.currentRoom.drop(item);
    item.onDrop();
  }

  public lookNorth() {
    return this.currentRoom.north;
  }

  public lookSouth() {
    return this.currentRoom.south;
  }

  public lookEast() {
    return this.currentRoom.east;
  }

  public lookWest() {
    return this.currentRoom.west;
  }

  public itemSearch() {
    const items = this.currentRoom.items;
    return items.length > 0 ? items : null;
  }

  public bagSearch() {
    const items = this.items;
    return items.length > 0 ? items : null;
  }
}
