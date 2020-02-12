import { Entity } from './entity';
import { confirm } from './utils';

export class Item extends Entity {
  public toString() {
    return `\nItem: ${this.name} - ${this.description}`;
  }

  public hasName(name: string) {
    return this.name.toLowerCase() === name.toLowerCase();
  }

  public async onTake() {
    console.log(`You picked up ${this.name}`);
    await confirm();
  }

  public async onDrop() {
    console.log(`You dropped up ${this.name}`);
    await confirm();
  }
}
