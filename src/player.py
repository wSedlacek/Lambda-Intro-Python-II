from utils import clear


class Player:
    _name = None
    _current_room = None
    _items = []

    def __init__(self, name, room):
        self._name = name
        self._current_room = room

    def __str__(self):
        details = f'''==={self._name}==='''
        for item in self._items:
            details += str(item)
        details += '\n\n'
        return details

    def look(self):
        print(self._current_room)

    def move(self, room):
        self._current_room = room

    def inventory(self):
        clear()
        print(self)
        input('Press ENTER key to continue...')

    def take(self, item_name):
        items = self._current_room.items()
        item = next((item for item in items if item.has_name(item_name)))
        self._current_room.take(item)
        self._items.append(item)
        item.on_take()

    def drop(self, item_name):
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
