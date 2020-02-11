class Player:
    name = None
    current_room = None

    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def move(self, room):
        self.current_room = room

    def look_north(self):
        return self.current_room.north

    def look_south(self):
        return self.current_room.south

    def look_east(self):
        return self.current_room.east

    def look_west(self):
        return self.current_room.west
