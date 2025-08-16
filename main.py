import pygame, sys
pygame.init()

width = 400
height = 600

win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

pygame.display.set_caption("Flappy Bird")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((135, 206, 235))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()