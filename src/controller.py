from player import Player
from utils import clear


class Controller:
    _player: Player

    def __init__(self, player: Player):
        self._player = player

    def _build_prompt(self):
        prompt = '\nWhat will you do?'
        prompt += '\n  q - Quit'
        prompt += '\n  i - Inventory'

        if self._player.room().north():
            prompt += '\n  n - Move North'

        if self._player.room().south():
            prompt += '\n  s - Move South'

        if self._player.room().east():
            prompt += '\n  e - Move East'

        if self._player.room().west():
            prompt += '\n  w - Move West'

        if self._player.room().items():
            prompt += '\n  take <item> - Take a item from this room'

        if self._player.items():
            prompt += '\n  drop <item> - Drop a item in this room'

        prompt += '\n\nCommand: '
        return prompt

    def tick(self):
        command = input(self._build_prompt())
        action, *subjects = command.split(' ', 1)

        try:

            if action == 'n' or action == 's' or action == 'e' or action == 'w':
                self._player.move(action)
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
