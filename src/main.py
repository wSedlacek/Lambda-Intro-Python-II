import os

from room import Room
from player import Player
from controller import Controller

room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons'),

    'foyer':    Room('Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.'''),

    'overlook': Room('Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.'''),

    'narrow':   Room('Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.'''),

    'treasure': Room('Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.'''),
}

room['outside'].south_of(room['foyer'])
room['foyer'].south_of(room['overlook'])
room['foyer'].west_of(room['narrow'])
room['narrow'].south_of(room['treasure'])

player_name = input("What is your name adventurer? ")
player = Player(player_name, room['outside'])
controller = Controller(player)


#
# Main
#
command = "start"
while (command is not 'q'):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(player.current_room)
    command = controller.tick()
