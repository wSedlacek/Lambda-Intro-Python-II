class Controller:
    player = None
    prompt_question = '\n\nWhat will you do?'
    prompt_north = '\n  n - Move North'
    prompt_south = '\n  s - Move South'
    prompt_west = '\n  w - Move West'
    prompt_east = '\n  e - Move East'
    prompt_quit = '\n  q - Quit'
    prompt = '\n\nCommand: '

    def __init__(self, player):
        self.player = player

    def tick(self):
        prompt = self.prompt_question
        if self.player.current_room.north is not None:
            prompt += self.prompt_north

        if self.player.current_room.south is not None:
            prompt += self.prompt_south

        if self.player.current_room.east is not None:
            prompt += self.prompt_east

        if self.player.current_room.west is not None:
            prompt += self.prompt_west

        prompt += self.prompt_quit
        prompt += self.prompt
        command = input(prompt)
        move_to = None

        if command is 'n':
            move_to = self.player.current_room.north

        if command is 's':
            move_to = self.player.current_room.south

        if command is 'e':
            move_to = self.player.current_room.east

        if command is 'w':
            move_to = self.player.current_room.west

        if command is 'q':
            return command

        if move_to is not None:
            self.player.current_room = move_to
            return command

        input("INVALID COMMAND! Press any key then enter a valid command...")
