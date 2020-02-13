import { Item } from '../base/item';

export class Money extends Item {
  public readonly value: number;
  constructor(name: string, description: string, value: number) {
    super(name, description);
    this.value = value;
  }
}
