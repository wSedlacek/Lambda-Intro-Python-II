class Item:
    _name: str
    _description: str

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    def __str__(self):
        return f'''\nItem: {self._name} - {self._description}'''

    def has_name(self, name: str):
        return self._name.lower() == name.lower()

    def on_take(self):
        print(f'You picked up {self._name}')
        input('Press ENTER key to continue...')

    def on_drop(self):
        print(f'You dropped {self._name}')
        input('Press ENTER key to continue...')
