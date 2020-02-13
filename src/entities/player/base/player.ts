import { Entity, Item, Room } from '../..';

export class Player extends Entity {
  private currentRoom: Room;
  private readonly items: Item[];

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

  public move(direction: 'n' | 'north' | 's' | 'south' | 'e' | 'east' | 'w' | 'west') {
    if (direction === 'n') direction = 'north';
    if (direction === 's') direction = 'south';
    if (direction === 'e') direction = 'east';
    if (direction === 'w') direction = 'west';

    let room = this.currentRoom[direction];
    if (!room) throw new Error('INVALID ROOM!');
    this.currentRoom = room;
  }

  public take(itemName: string) {
    const index = this.currentRoom.items.findIndex((item) => item.hasName(itemName));
    if (index === -1) throw new Error('INVALID ITEM!');
    const [item] = this.currentRoom.take(index);
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
