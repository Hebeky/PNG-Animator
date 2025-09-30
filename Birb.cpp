import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bird1 = pygame.image.load("bird1.png")
bird2 = pygame.image.load("bird2.png")

pos_x, pos_y = 100, 300
frame = 0

running = True
while running:
for event in pygame.event.get() :
    if event.type == pygame.QUIT :
        running = False

        frame += 1
        if (frame // 20) % 2 == 0:
            bird = bird1
        else:
bird = bird2

pos_x += 1  # move bird to the right

screen.fill((255, 255, 255))   # white background
screen.blit(bird, (pos_x, pos_y))
pygame.display.flip()

clock.tick(60)

pygame.quit()
