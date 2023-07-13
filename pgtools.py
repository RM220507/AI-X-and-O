import pygame

def quit_check(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
