import pygame, sys
from simulation import Simulation

pygame.init()

# Static vars

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 12
FPS = 12

# Set window resolution in pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Window Title
pygame.display.set_caption("Game of Life")

# time.Clock() method tracks an amount of time
# In this instance it is used to control the game's fps
clock = pygame.time.Clock()

# Main Loop
while True:
    
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # 2. Update State

    # 3. Draw
    window.fill(GREY)
    pygame.display.update()
    clock.tick(FPS)
