import customtkinter as ctk
from human import Human
from minimax import Minimax

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Minimax Noughts & Crosses")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #self.iconphoto(False, tk.PhotoImage(file="icon.png"))
        self.geometry(f"{600}x{600}")

        self.w = 3
        self.h = 3

        self.players = [Human(self, "X"), Minimax(self, "O", "X")]
        self.player_index = -1
        self.spaces_free = self.w * self.h

        self.board_frame = ctk.CTkFrame(self)
        self.board_frame.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="NSEW")
        self.board_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.board_frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.position_labels = [[ctk.CTkButton(self.board_frame, text="-", font=ctk.CTkFont("sans-serif", 50), command=lambda i=i, j=j: self.players[self.player_index].button_pressed(j, i))  for i in range(3)] for j in range(3)]

        for i in range(self.w):
            for j in range(self.h):
                self.position_labels[i][j].grid(row=i, column=j, padx=20, pady=(20, 20), sticky="NSEW")

        self.status_frame = ctk.CTkFrame(self)
        self.status_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="EW")

        self.status_label = ctk.CTkLabel(self.status_frame, text="", font=ctk.CTkFont("sans-serif", 30))
        self.status_label.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.next_player()

    def next_player(self):
        self.player_index = (self.player_index + 1) % 2
        player = self.players[self.player_index]

        self.status_label.configure(text=f"{player.label}'s Turn")
        self.update()

        player.take_turn(self.gamestate())

    def gamestate(self):
        return [[self.position_labels[i][j].cget("text") for j in range(3)] for i in range(3)]

    def game_end(self, gamestate):
        runs = []

        runs.extend(gamestate) # rows

        for col_num in range(self.w):
            runs.append([gamestate[0][col_num], gamestate[1][col_num], gamestate[2][col_num]]) # columns

        runs.append([gamestate[0][0], gamestate[1][1], gamestate[2][2]]) # diagonal 1
        runs.append([gamestate[0][2], gamestate[1][1], gamestate[2][0]]) # diagonal 2

        for run in runs:
            if run[0] == run[1] == run[2] and run[0] != "-":
                return True, run[0]
        
        free_spaces = 0
        for row in range(self.h):
            free_spaces += gamestate[row].count("-")

        if free_spaces == 0:
            return True, None        
        
        return False, None
    
    def set_tile(self, change, label):
        self.position_labels[change[0]][change[1]].configure(text=label)

        game_ended, winner = self.game_end(self.gamestate())
        if game_ended:
            if not winner:
                self.status_label.configure(text="It's a Draw!")
            else:
                self.status_label.configure(text=f"{winner} Wins!")
        else:
            self.spaces_free -= 1
            self.next_player()

if __name__ == "__main__":
    app = App()
    app.mainloop()

    