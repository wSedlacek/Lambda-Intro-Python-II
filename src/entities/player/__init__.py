from typing import List, Optional

from .. import Entity
from ..items import Item
from ..room import Room


class Player(Entity):
    _current_room: Room
    _items: List[Item]

    def __init__(self, name: str, room: Room):
        super().__init__(name, "PC")
        self._current_room = room
        self._items = []

    def __str__(self):
        details = f'''==={self.name}==='''
        for item in self._items:
            details += str(item)
        details += '\n\n'
        return details

    def look(self):
        print(self._current_room)

    def move(self, room: Optional[Room]):
        if room is None:
            raise TypeError
        self._current_room = room

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

    def look_north(self):
        return self._current_room.north()

    def look_south(self):
        return self._current_room.south()

    def look_east(self):
        return self._current_room.east()

    def look_west(self):
        return self._current_room.west()

    def item_search(self):
        if len(self._current_room.items()) is 0:
            return None
        else:
            return self._current_room.items()

    def bag_search(self):
        if len(self._items) is 0:
            return None
        else:
            return self._items
