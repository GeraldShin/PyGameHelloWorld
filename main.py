import pygame
import sys # Import the sys module for exiting the program
import colors_shortcuts as colors
import os

pygame.init()
FONT = pygame.font.SysFont("Verdana", 20)

# Set window dimensions
game_width = 800
game_height = 600
window_surface = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('SHINLOLS GAME HELLO WORLD')
center_pos = pygame.Vector2(window_surface.get_width() / 2, window_surface.get_height() / 2)
# Dead center

clock = pygame.time.Clock()
FPS_LIMIT = 60
# we don't really need to keep this in here, it's just so my pc doesnt explode

# Set music and vibes
# Do we need different load calls to set different themes/songs?
try:
    pygame.mixer.music.load(os.getcwd() + "\\sounds\\themes\\song18.mp3")
    pygame.mixer.music.set_volume(0.05) # we set this to 0 for now so ms beans doesnt get annoyed
    pygame.mixer.music.play(-1)
except pygame.error:
    print('Music not available or could not be loaded')
    running = False

# Importing Sprite Sheet
axe_sprite = pygame.image.load(os.getcwd() +"\\image_assets\\RavenmoreIconPack.02.2014\\64\\axe.png")
sprite_sheet = pygame.image.load(os.getcwd() + "\\image_assets\\ProjectUtumno_full.png")

def get_image(sheet, x, y, width, height):
    """Extracts an image from a sprite sheet."""
    # Create a new blank Surface for the individual sprite
    image = pygame.Surface([width, height]).convert_alpha()
    # Blit the desired area from the main sheet onto the new surface
    image.blit(sheet, (0, 0), (x, y, width, height))
    # Optional: Set a color key for transparency if your sheet has a solid background color
    # image.set_colorkey((0, 0, 0)) # Assuming black is the background color
    return image

# Example for a sheet with 32x32 pixel sprites arranged in a grid
sprite_width = 32
sprite_height = 32
num_sprites_x = sprite_sheet.get_width() // sprite_width
num_sprites_y = sprite_sheet.get_height() // sprite_height

animation_frames = []

for row in range(num_sprites_y):
    for col in range(num_sprites_x):
        x = col * sprite_width
        y = row * sprite_height
        # Extract the image using the function defined above
        image = get_image(sprite_sheet, x, y, sprite_width, sprite_height)
        animation_frames.append(image)
        # animation_frames now contains a list of individual sprite images

moving_rect = axe_sprite.get_rect()
# Create a surface for the background
background = pygame.Surface((game_width, game_height))
background.fill(colors.BLACK)

boss_title_text_surface = FONT.render("BIG BOSS CIRCLE", True, colors.WHITE)
boss_hp_var = 50000


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Draw the background
    window_surface.blit(background, (0, 0))
    circle = pygame.draw.circle(window_surface, "red", center_pos, 40)
    window_surface.blit(boss_title_text_surface, (circle.x*0.85, circle.y*1.35))
    boss_health_text_surface = FONT.render(text=str(boss_hp_var), antialias=True, color=colors.WHITE)
    boss_hp_text_rect = window_surface.blit(boss_health_text_surface, (circle.x*0.85, circle.y*.75))
    fps_value = clock.get_fps()

    fps_surface = FONT.render(f"FPS: {fps_value:.2f}", True, colors.WHITE)
    window_surface.blit(fps_surface, fps_surface.get_rect(bottomright = window_surface.get_rect().bottomright))

    speed = 10
    axe_damage = 50

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed
    if keys[pygame.K_UP]:
        moving_rect.y -= speed
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed

    moving_rect.x = max(0, min(moving_rect.x, game_width - moving_rect.width))
    moving_rect.y = max(0, min(moving_rect.y, game_height - moving_rect.height))


    window_surface.blit(axe_sprite, moving_rect)

    if moving_rect.colliderect(circle):
        boss_hp_var -= axe_damage
        pygame.display.update(boss_hp_text_rect)
    # Update the display
    pygame.display.flip()

    # pygame.display.update() # UPDATE will update the entire screen. You can update parts with flip, including the entire screen.
                              # Like if you wanted to refresh just one icon instead of the entire screen, you'd need flip anyways
    clock.tick(FPS_LIMIT)
# Quit pygame and exit the program
pygame.quit()
sys.exit()
