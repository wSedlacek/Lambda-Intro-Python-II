from typing import List, Optional

from entity import Entity
from item import Item
from room import Room


class Player(Entity):
    _current_room: Room
    _items: List[Item]

    def __init__(self, name: str, room: Room):
        super().__init__(name, "PC")
        self._current_room = room
        self._items = []

    def __str__(self):
        details = f'==={self.name}==='
        for item in self._items:
            details += str(item)
        details += '\n\n'
        return details

    def look(self):
        print(self._current_room)

    def move(self, direction: str):
        if direction is 'n':
            direction = 'north'

        if direction is 's':
            direction = 'south'

        if direction is 'e':
            direction = 'east'

        if direction is 'w':
            direction = 'west'

        room = getattr(self._current_room, direction)

        if not room():
            raise TypeError

        self._current_room = room()

    def inventory(self):
        print(self)
        input('Press ENTER key to continue...')

    def take(self, item_name: str):
        items = self._current_room.items()
        item = next((item for item in items if item.has_name(item_name)))
        self._current_room.take(item)
        self._items.append(item)
        item.on_take()

    def drop(self, item_name: str):
        items = self._items
        item = next((item for item in items if item.has_name(item_name)))
        self._items.remove(item)
        self._current_room.drop(item)
        item.on_drop()

    def room(self):
        return self._current_room

    def items(self):
        return self._items
