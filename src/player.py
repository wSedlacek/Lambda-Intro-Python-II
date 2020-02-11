from utils import clear


class Player:
    name = None
    current_room = None
    items = []

    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def __str__(self):
        details = f'''==={self.name}==='''
        for item in self.items:
            details += f'''\nItem: {item.name} - {item.description}'''
        details += '\n\n'
        return details

    def move(self, room):
        self.current_room = room

    def inventory(self):
        clear()
        print(self)
        input('Press ENTER key to continue...')

    def take(self, item_name):
        def is_the_item(item):
            return item.name.lower() == item_name.lower()

        items = self.current_room.items
        item = next((item for item in items if is_the_item(item)))
        self.current_room.items.remove(item)
        self.items.append(item)
        item.on_take()

    def drop(self, item_name):
        def is_the_item(item):
            return item.name.lower() == item_name.lower()

        items = self.items
        item = next((item for item in items if is_the_item(item)))
        self.items.remove(item)
        self.current_room.items.append(item)
        item.on_drop()

    def look_north(self):
        return self.current_room.north

    def look_south(self):
        return self.current_room.south

    def look_east(self):
        return self.current_room.east

    def look_west(self):
        return self.current_room.west

    def item_search(self):
        if len(self.current_room.items) is 0:
            return None
        else:
            return self.current_room.items

    def bag_search(self):
        if len(self.items) is 0:
            return None
        else:
            return self.items
