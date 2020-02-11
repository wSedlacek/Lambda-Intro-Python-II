class Controller:
    _player = None
    _prompt_question = '\nWhat will you do?'
    _prompt_quit = '\n  q - Quit'
    _prompt_inventory = '\n  i - Inventory'
    _prompt_north = '\n  n - Move North'
    _prompt_south = '\n  s - Move South'
    _prompt_west = '\n  w - Move West'
    _prompt_east = '\n  e - Move East'
    _prompt_take = '\n  take <item> - Take a item from this room'
    _prompt_drop = '\n  drop <item> - Drop a item in this room'
    _prompt = '\n\nCommand: '

    def __init__(self, player):
        self._player = player

    def _build_prompt(self):
        prompt = self._prompt_question
        prompt += self._prompt_quit
        prompt += self._prompt_inventory

        if self._player.look_north() is not None:
            prompt += self._prompt_north

        if self._player.look_south() is not None:
            prompt += self._prompt_south

        if self._player.look_east() is not None:
            prompt += self._prompt_east

        if self._player.look_west() is not None:
            prompt += self._prompt_west

        if self._player.item_search() is not None:
            prompt += self._prompt_take

        if self._player.bag_search() is not None:
            prompt += self._prompt_drop

        prompt += self._prompt
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
