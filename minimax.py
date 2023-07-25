from copy import deepcopy

class Minimax:
    def __init__(self, app, label, opponent_label):
        self.label = label
        self.app = app
        self.opponent_label = opponent_label

    def take_turn(self, gamestate):
        node = Node(gamestate, None)

        best_score = float("-inf")
        best_move = None

        depth = 0
        for row in gamestate:
            depth += row.count("-")

        for child in node.gen_children(self.label):
            #print(child.gamestate)
            score = self.minimax(child, depth - 1, False)
            #print("Score:", score)
            if score > best_score:
                best_score = score
                best_move = child.change

        self.app.set_tile(best_move, self.label)

    def evaluate_board(self, board, depth):
        # Check for a win
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != "-":
                return 10 - depth if row[0] == self.label else depth - 10

        for col in range(len(board)):
            if all(board[row][col] == board[0][col] and board[0][col] != "-" for row in range(len(board))):
                return 10 if board[0][col] == self.label else -10

        if all(board[i][i] == board[0][0] and board[0][0] != "-" for i in range(len(board))):
            return 10 if board[0][0] == self.label else -10

        if all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] and board[0][len(board) - 1] != "-" for i in range(len(board))):
            return 10 if board[0][len(board) - 1] == self.label else -10

        return 0
    
    def minimax(self, node, depth, maximising : bool):
        #print("Running - depth:", depth)
        if depth == 0 or self.evaluate_board(node.gamestate, depth) != 0:
            return self.evaluate_board(node.gamestate, depth)
            
        if maximising:
            value = float("-inf")
            for child in node.gen_children(self.label):
                value = max(value, self.minimax(child, depth - 1, False))
            return value
        else:
            value = float("inf")
            for child in node.gen_children(self.opponent_label):
                value = min(value, self.minimax(child, depth - 1, True))
            return value

    def button_pressed(self, i, j):
        pass

class Node:
    def __init__(self, gamestate, change):
        self.gamestate = gamestate
        self.change = change

    def gen_children(self, label):
        self.children = []
        for i in range(len(self.gamestate)):
            for j in range(len(self.gamestate[i])):
                if self.gamestate[i][j] == "-":
                    next_state = deepcopy(self.gamestate)
                    next_state[i][j] = label
                    child = Node(next_state, (i, j))
                    self.children.append(child)
        return self.children
