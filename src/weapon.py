from item import Item


class Weapon(Item):
    power: int

    def __init__(self, name: str, description: str, power: int):
        super().__init__(name, description)
        self.power = power
