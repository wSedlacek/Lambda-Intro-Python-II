from entities.player import Player
from utils import clear


class Controller:
    _player: Player

    def __init__(self, player: Player):
        self._player = player

    def _build_prompt(self):
        prompt = '\nWhat will you do?'
        prompt += '\n  q - Quit'
        prompt += '\n  i - Inventory'

        if self._player.look_north():
            prompt += '\n  n - Move North'

        if self._player.look_south():
            prompt += '\n  s - Move South'

        if self._player.look_east():
            prompt += '\n  e - Move East'

        if self._player.look_west():
            prompt += '\n  w - Move West'

        if self._player.item_search():
            prompt += '\n  take <item> - Take a item from this room'

        if self._player.bag_search():
            prompt += '\n  drop <item> - Drop a item in this room'

        prompt += '\n\nCommand: '
        return prompt

    def tick(self):
        command = input(self._build_prompt())
        action, *subjects = command.split(' ', 1)

        try:
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

            if action == 'take' or action == 'get':
                self._player.take(subjects[0])
                return command

            if action == 'drop':
                self._player.drop(subjects[0])
                return command

            if action == 'i' or action == 'inventory':
                clear()
                self._player.inventory()
                return command

            if action == 'q' or action == 'quit':
                return command

            raise NotImplementedError
        except:
            input("INVALID COMMAND! Press ENTER key then enter a valid command...")

    def start(self):
        command = "start"
        while (command is not 'q'):
            clear()
            self._player.look()
            command = self.tick()
