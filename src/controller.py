class Controller:
    _player = None

    def __init__(self, player):
        self._player = player

    def _build_prompt(self):
        prompt = '\nWhat will you do?'
        prompt += '\n  q - Quit'
        prompt += '\n  i - Inventory'

        if self._player.look_north() is not None:
            prompt += '\n  n - Move North'

        if self._player.look_south() is not None:
            prompt += '\n  s - Move South'

        if self._player.look_east() is not None:
            prompt += '\n  e - Move East'

        if self._player.look_west() is not None:
            prompt += '\n  w - Move West'

        if self._player.item_search() is not None:
            prompt += '\n  take <item> - Take a item from this room'

        if self._player.bag_search() is not None:
            prompt += '\n  drop <item> - Drop a item in this room'

        prompt += '\n\nCommand: '
        return prompt

    def tick(self):
        command = input(self._build_prompt())
        action, *subjects = command.split(' ', 1)

        if action == 'n':
            room = self._player.look_north()
            self._player.move(room)
            return command

        if action == 's':
            room = self._player.look_south()
            self._player.move(room)
            return command

        if action == 'e':
            room = self._player.look_east()
            self._player.move(room)
            return command

        if action == 'w':
            room = self._player.look_west()
            self._player.move(room)
            return command

        if action == 'take':
            try:
                self._player.take(subjects[0])
                return command
            except:
                input("INVALID ITEM! Press ENTER key then enter a valid command...")
                return command

        if action == 'drop':
            try:
                self._player.drop(subjects[0])
                return command
            except:
                input("INVALID ITEM! Press ENTER key then enter a valid command...")
                return command

        if action == 'i':
            self._player.inventory()
            return command

        if action == 'q':
            return command

        input("INVALID COMMAND! Press ENTER key then enter a valid command...")
