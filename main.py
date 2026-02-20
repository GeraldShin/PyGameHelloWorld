import pygame
import sys # Import the sys module for exiting the program

pygame.init()

# Set window dimensions
game_width = 800
game_height = 600
window_surface = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Quick Start')
FramePerSec = pygame.time.Clock()
# Define colors
background_color = pygame.Color('#000000') # Black color

# Create a surface for the background
background = pygame.Surface((game_width, game_height))
background.fill(background_color)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Draw the background
    window_surface.blit(background, (0, 0))

    # Update the display
    pygame.display.update()

# Quit pygame and exit the program
pygame.quit()
sys.exit()
