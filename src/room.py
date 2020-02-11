class Room:
    _name = None
    _description = None

    _north = None
    _south = None
    _east = None
    _west = None

    _items = None

    def __init__(self, name, description, items):
        self._name = name
        self._description = description
        self._items = items

    def __str__(self):
        details = f'''==={self._name}===
{self._description}\n'''

        for item in self._items:
            details += str(item)

        return details

    def north_of(self, room):
        room._north = self
        self._south = room

    def south_of(self, room):
        room._south = self
        self._north = room

    def east_of(self, room):
        room._east = self
        self._west = room

    def west_of(self, room):
        room._west = self
        self._east = room

    def items(self):
        return self._items

    def take(self, item):
        self._items.remove(item)

    def drop(self, item):
        self._items.append(item)

    def north(self):
        return self._north

    def south(self):
        return self._south

    def east(self):
        return self._east

    def west(self):
        return self._west
