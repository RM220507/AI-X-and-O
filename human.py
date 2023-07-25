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
                self.app.set_tile((i, j), self.label)