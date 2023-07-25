import customtkinter as ctk
from players import Human, Minimax

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Minimax Noughts & Crosses")
        #self.iconphoto(False, tk.PhotoImage(file="icon.png"))
        self.geometry(f"{600}x{600}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        human_player = Human(self, "X")
        self.players = [human_player, Minimax(self, "O", human_player)]
        self.player_index = 0

        self.position_labels = [[ctk.CTkButton(self, text="-", command=lambda i=i, j=j: self.players[self.player_index].button_pressed(i, j))  for i in range(3)] for j in range(3)]

        for i in range(3):
            for j in range(3):
                self.position_labels[i][j].grid(row=i, column=j, padx=20, pady=(20, 20), sticky="NSEW")

        self.players[self.player_index].take_turn(self.gamestate())

    def gamestate(self):
        return [[self.position_labels[i][j].cget("text") for j in range(3)] for i in range(3)]

    def game_won(self, gamestate):
        return False, []
    
    def set_tile(self, i, j, label):
        self.position_labels[i][j].configure(text=label)

        if self.game_won():
            pass
        else:
            self.player_index = (self.player_index + 1) % 2
            self.players[self.player_index].take_turn(self.gamestate())

if __name__ == "__main__":
    app = App()
    app.mainloop()

    