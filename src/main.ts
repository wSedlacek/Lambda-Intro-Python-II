import { Controller } from './controller';
import { Item } from './item';
import { Player } from './player';
import { Room } from './room';
import { prompt } from './utils';

const items = {
  sword: new Item('Sword', 'A sharp toy to cut things.'),
  coins: new Item('Coins', 'A sum of coins...')
};

const rooms = {
  outside: new Room('Outside Cave Entrance', 'North of you, the cave mount beckons', [items.sword]),
  foyer: new Room(
    'Foyer',
    `Dim light filters in from the south. Dusty
passages run north and east.`
  ),
  overlook: new Room(
    'Grand Overlook',
    `A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.`
  ),
  narrow: new Room(
    'Narrow Passage',
    `The narrow passage bends here from west
to north. The smell of gold permeates the air.`
  ),
  treasure: new Room(
    'Treasure Chamber',
    `You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.`,
    [items.coins]
  )
};

rooms.outside.southOf(rooms.foyer);
rooms.foyer.southOf(rooms.overlook);
rooms.foyer.westOf(rooms.narrow);
rooms.narrow.southOf(rooms.treasure);

const main = async () => {
  const response = await prompt('What is your name adventurer?');
  const player = new Player(response.text, rooms.outside);
  const controller = new Controller(player);
  await controller.loop();
};

main();
