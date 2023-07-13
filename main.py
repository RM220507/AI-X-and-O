import pygame
from pgtools import *
from players import *

pygame.init()

display = pygame.display.set_mode((800, 800))

cell_size = 200
board_start = (100, 100)

players = [AI("X"), Human("O")]

current_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def mainloop():
    running = True
    while running:
        display.fill(0)

        # check events
        for event in pygame.event.get():
            quit_check(event)

        # draw board
        pygame.draw.line(display, (255, 255, 255), (board_start[0], board_start[1] + cell_size), (board_start[0] + 3 * cell_size, board_start[1] + cell_size))
        pygame.draw.line(display, (255, 255, 255), (board_start[0] + cell_size, board_start[1]), (board_start[0] + cell_size, board_start[1] + 3 * cell_size))
        pygame.draw.line(display, (255, 255, 255), (board_start[0], board_start[1] + 2 * cell_size), (board_start[0] + 3 * cell_size, board_start[1] + 2 * cell_size))
        pygame.draw.line(display, (255, 255, 255), (board_start[0] + 2 * cell_size, board_start[1]), (board_start[0] + 2 * cell_size, board_start[1] + 3 * cell_size))

        pygame.display.update()

mainloop()
