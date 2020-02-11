class Room:
    name = None
    description = None

    north = None
    south = None
    east = None
    west = None

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'''==={self.name}===
{self.description}'''

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
