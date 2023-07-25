class Minimax:
    def __init__(self, app, label, opponent):
        self.label = label
        self.app = app
        self.opponent = opponent

    def take_turn(self, gamestate):
        # locate gamestate in gamestate_data
        # calculate best move, based on choice_probabilities
        # add move to path, for bonus/punishment later
        pass

    def minimax(self, gamestate, depth, maximising : bool):
        terminate, player = self.app.game_won(gamestate)
        if depth == 0:
            return 0
        elif terminate:
            if player == 0:
                return -1
            elif player == 1:
                return 1
            
        if maximising:
            value = float("-inf")
            for next_move in self.get_next_moves(gamestate, self.label):
                pass

    def get_next_moves(self, gamestate):
        pass

    def button_pressed(self, i, j):
        pass

class Human:
    def __init__(self, app, label):
        self.label = label
        self.app = app

        self.waiting = False

    def take_turn(self, gamestate):
        self.waiting = True
        self.gamestate = gamestate

    def button_pressed(self, i, j):
        if self.waiting:
            if self.gamestate[i][j] == "-":
                self.waiting = False
                self.app.set_tile(i, j, self.label)