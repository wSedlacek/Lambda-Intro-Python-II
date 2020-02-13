export abstract class Entity extends Object {
  constructor(public readonly name: string, public readonly description: string) {
    super();
  }
}
