from room import Room
from item import Item
from player import Player
from controller import Controller


items = {
    'sword': Item("Sword", "A sharp toy to cut things.")
}

rooms = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons',
                     [items['sword']]),

    'foyer':    Room('Foyer',
                     '''Dim light filters in from the south. Dusty
passages run north and east.''',
                     []),

    'overlook': Room('Grand Overlook',
                     '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.''',
                     []),

    'narrow':   Room('Narrow Passage',
                     '''The narrow passage bends here from west
to north. The smell of gold permeates the air.''',
                     []),

    'treasure': Room('Treasure Chamber',
                     '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.''',
                     []),
}

rooms['outside'].south_of(rooms['foyer'])
rooms['foyer'].south_of(rooms['overlook'])
rooms['foyer'].west_of(rooms['narrow'])
rooms['narrow'].south_of(rooms['treasure'])

player_name = input("What is your name adventurer?\n")
player = Player(player_name, rooms['outside'])
controller = Controller(player)
controller.start()
