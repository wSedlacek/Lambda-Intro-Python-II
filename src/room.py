class Room:
    name = None
    description = None

    north = None
    south = None
    east = None
    west = None

    items = None

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        details = f'''==={self.name}===
{self.description}\n'''

        for item in self.items:
            details += f'''\nItem: {item.name} - {item.description}'''

        return details

    def north_of(self, room):
        room.north = self
        self.south = room

    def south_of(self, room):
        room.south = self
        self.north = room

    def east_of(self, room):
        room.east = self
        self.west = room

    def west_of(self, room):
        room.west = self
        self.east = room
