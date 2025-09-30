"""
Pixel Bird Animation
--------------------
A simple Pygame script that animates a pixel bird sprite flapping its wings
and bouncing back and forth across the screen.
"""

import pygame

# --- Configuration ---
WIDTH, HEIGHT = 800, 600   # window dimensions
FPS = 60                   # frames per second (loop speed)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- Load frames ---
# LEFT-facing bird animation (4 frames of wing movement).
frames_left = [
    pygame.image.load("Birb1.png").convert_alpha(),
    pygame.image.load("Birb2.png").convert_alpha(),
    pygame.image.load("Birb3.png").convert_alpha(),
    pygame.image.load("Birb4.png").convert_alpha(),
]

# RIGHT-facing frames generated automatically by flipping horizontally.
frames_right = [pygame.transform.flip(f, True, False) for f in frames_left]

# --- Bird state ---
pos_x, pos_y = 100, 300    # initial position
speed_x = 2                # horizontal speed
frame_index = 0            # current animation frame
frame_counter = 0          # counter to control frame switching
frame_speed = 30           # lower = faster flapping

bird_width  = frames_left[0].get_width()
bird_height = frames_left[0].get_height()

# --- Main loop ---
running = True
while running:
    # Handle events (quit button, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Animate ---
    frame_counter += 1
    if frame_counter >= frame_speed:
        frame_counter = 0
        frame_index = (frame_index + 1) % len(frames_left)

    # Pick correct frame set based on direction
    # If speed_x > 0 → moving right → use right-facing frames.
    # If speed_x < 0 → moving left → use left-facing frames.
    current_frames = frames_right if speed_x > 0 else frames_left
    current_frame = current_frames[frame_index]

    # --- Move ---
    pos_x += speed_x

    # --- Collisions with screen edges (bounce) ---
    if pos_x <= 0:
        pos_x = 0
        speed_x = abs(speed_x)  # ensure moving right
    elif pos_x >= WIDTH - bird_width:
        pos_x = WIDTH - bird_width
        speed_x = -abs(speed_x) # ensure moving left

    # --- Draw ---
    screen.fill((200, 230, 255))        # sky-blue background, can be altered
    screen.blit(current_frame, (pos_x, pos_y))
    pygame.display.flip()

    clock.tick(FPS)  # maintain FPS speed

pygame.quit()
