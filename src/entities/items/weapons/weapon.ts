import { Item } from '..';

export class Weapon extends Item {
  public readonly power: number;
  constructor(name: string, description: string, power: number) {
    super(name, description);
    this.power = power;
  }
}
