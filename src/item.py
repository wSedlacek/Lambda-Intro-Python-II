from entity import Entity


class Item(Entity):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def __str__(self):
        return f'''\nItem: {self.name} - {self.description}'''

    def has_name(self, name: str):
        return self.name.lower() == name.lower()

    def on_take(self):
        print(f'You picked up {self.name}')
        input('Press ENTER key to continue...')

    def on_drop(self):
        print(f'You dropped {self.name}')
        input('Press ENTER key to continue...')
