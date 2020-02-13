from __future__ import annotations
from typing import List, Optional

from .. import Entity
from ..items import Item


class Room(Entity):
    _north: Optional["Room"]
    _south: Optional["Room"]
    _east: Optional["Room"]
    _west: Optional["Room"]

    _items: List[Item]

    def __init__(self, name: str, description: str, items: List[Item] = []):
        super().__init__(name, description)
        self._items = items
        self._north = None
        self._south = None
        self._east = None
        self._west = None

    def __str__(self):
        details = f'''==={self.name}===
{self.description}\n'''

        for item in self._items:
            details += str(item)

        return details

    def north_of(self, room: Room):
        room._north = self
        self._south = room

    def south_of(self, room: Room):
        room._south = self
        self._north = room

    def east_of(self, room: Room):
        room._east = self
        self._west = room

    def west_of(self, room: Room):
        room._west = self
        self._east = room

    def items(self):
        if len(self._items) is 0:
            return None
        else:
            return self._items

    def take(self, item: Item):
        self._items.remove(item)

    def drop(self, item: Item):
        self._items.append(item)

    def north(self):
        return self._north

    def south(self):
        return self._south

    def east(self):
        return self._east

    def west(self):
        return self._west
