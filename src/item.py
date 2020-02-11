class Item:
    name = None
    description = None

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You picked up {self.name}')
        input('Press ENTER key to continue...')

    def on_drop(self):
        print(f'You dropped {self.name}')
        input('Press ENTER key to continue...')
