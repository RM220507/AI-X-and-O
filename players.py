import json

BLANK = " "

class AI:
    def __init__(self, player):
        self.gamestate_data = json.loads(open("gamestates_training.json", "r"))
        self.player = player

    def take_turn(self, gamestate):
        # locate gamestate in gamestate_data
        # calculate best move, based on choice_probabilities
        # add move to path, for bonus/punishment later
        pass

class Human:
    def __init__(self, player):
        self.player = player

    def take_turn(self, gamestate):
        # get mouse click, and work out which tile was clicked
        pass
