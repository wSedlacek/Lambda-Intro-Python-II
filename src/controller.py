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
        if self.player.look_north() is not None:
            prompt += self.prompt_north

        if self.player.look_south() is not None:
            prompt += self.prompt_south

        if self.player.look_east() is not None:
            prompt += self.prompt_east

        if self.player.look_west() is not None:
            prompt += self.prompt_west

        prompt += self.prompt_quit
        prompt += self.prompt
        command = input(prompt)
        move_to = None

        if command is 'n':
            move_to = self.player.look_north()

        if command is 's':
            move_to = self.player.look_south()

        if command is 'e':
            move_to = self.player.look_east()

        if command is 'w':
            move_to = self.player.look_west()

        if command is 'q':
            return command

        if move_to is not None:
            self.player.move(move_to)
            return command

        input("INVALID COMMAND! Press any key then enter a valid command...")
