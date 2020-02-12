import { Room } from './room';
import { Player } from './player';
import { confirm, prompt, invalid } from './utils';

export class Controller {
  constructor(private player: Player) {}

  private buildPrompt() {
    let prompt = 'What will you do?';
    prompt += '\n  q - Quit';
    prompt += '\n  i - Inventory';

    if (this.player.lookNorth()) prompt += '\n  n - Move North';
    if (this.player.lookSouth()) prompt += '\n  s - Move South';
    if (this.player.lookEast()) prompt += '\n  e - Move East';
    if (this.player.lookWest()) prompt += '\n  w - Move West';
    if (this.player.itemSearch()) prompt += '\n  take <item> - Take a item from this room';
    if (this.player.bagSearch()) prompt += '\n  drop <item> - Drop a item in this room';
    prompt += '\n\nCommand: ';

    return prompt;
  }

  private async tick() {
    const response = await prompt(this.buildPrompt());
    const [action, ...subjects] = response.text.split(' ', 2);

    try {
      let room: Room;
      switch (action) {
        case 'n':
          room = this.player.lookNorth();
          if (!room) throw new Error('INVALID ROOM!');
          else this.player.move(room);
          return response.text;

        case 's':
          room = this.player.lookSouth();
          if (!room) throw new Error('INVALID ROOM!');
          else this.player.move(room);
          return response.text;

        case 'e':
          room = this.player.lookEast();
          if (!room) throw new Error('INVALID ROOM!');
          else this.player.move(room);
          return response.text;

        case 'w':
          room = this.player.lookWest();
          if (!room) throw new Error('INVALID ROOM!');
          else this.player.move(room);
          return response.text;

        case 'get':
        case 'take':
          this.player.take(subjects[0]);
          return response.text;

        case 'drop':
          this.player.drop(subjects[0]);
          return response.text;

        case 'i':
        case 'inventory':
          console.clear();
          console.log(this.player.toString());
          await confirm();
          return response.text;

        case 'q':
          return response.text;

        default:
          throw new Error('INVALID COMMAND!');
      }
    } catch (err) {
      await invalid(err.message);
    }
  }

  public async loop() {
    let command;
    do {
      console.clear();
      console.log(this.player.look().toString());
      command = await this.tick();
    } while (command !== 'q');
  }
}
