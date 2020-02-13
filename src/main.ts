import { Controller } from './controller';
import { Room, Player, Money, Weapon } from './entities';
import { prompt } from './utils';

const items = {
  coins: new Money('Coins', 'A sum of coins...', 100),
  sword: new Weapon('Sword', 'A sharp toy to cut things.', 2)
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

rooms.outside.north = rooms.foyer;
rooms.foyer.north = rooms.overlook;
rooms.foyer.east = rooms.narrow;
rooms.narrow.north = rooms.treasure;

const main = async () => {
  const response = await prompt('What is your name adventurer?');
  const player = new Player(response.text, rooms.outside);
  const controller = new Controller(player);
  await controller.loop();
};

main();
