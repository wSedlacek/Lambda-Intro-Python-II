class Controller:
    player = None
    prompt_question = '\nWhat will you do?'
    prompt_quit = '\n  q - Quit'
    prompt_inventory = '\n  i - Inventory'
    prompt_north = '\n  n - Move North'
    prompt_south = '\n  s - Move South'
    prompt_west = '\n  w - Move West'
    prompt_east = '\n  e - Move East'
    prompt_take = '\n  take <item> - Take a item from this room'
    prompt_drop = '\n  drop <item> - Drop a item in this room'
    prompt = '\n\nCommand: '

    def __init__(self, player):
        self.player = player

    def build_prompt(self):
        prompt = self.prompt_question
        prompt += self.prompt_quit
        prompt += self.prompt_inventory

        if self.player.look_north() is not None:
            prompt += self.prompt_north

        if self.player.look_south() is not None:
            prompt += self.prompt_south

        if self.player.look_east() is not None:
            prompt += self.prompt_east

        if self.player.look_west() is not None:
            prompt += self.prompt_west

        if self.player.item_search() is not None:
            prompt += self.prompt_take

        if self.player.bag_search() is not None:
            prompt += self.prompt_drop

        prompt += self.prompt
        return prompt

    def tick(self):
        command = input(self.build_prompt())

        move_to = None

        if command is 'n':
            move_to = self.player.look_north()

        if command is 's':
            move_to = self.player.look_south()

        if command is 'e':
            move_to = self.player.look_east()

        if command is 'w':
            move_to = self.player.look_west()

        if command.startswith('take'):
            try:
                self.player.take(command.replace('take ', '', 1))
                return command
            except:
                input("INVALID ITEM! Press ENTER key then enter a valid command...")
                return command

        if command.startswith('drop'):
            try:
                self.player.drop(command.replace('drop ', '', 1))
                return command
            except:
                input("INVALID ITEM! Press ENTER key then enter a valid command...")
                return command

        if command is 'i':
            self.player.inventory()
            return command

        if command is 'q':
            return command

        if move_to is not None:
            self.player.move(move_to)
            return command

        input("INVALID COMMAND! Press ENTER key then enter a valid command...")
