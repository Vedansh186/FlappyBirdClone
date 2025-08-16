import pygame, sys
pygame.init()

width = 864
height = 936

win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


background = pygame.image.load("assets/bg.png")
pygame.display.set_caption("Flappy Bird")

run = True
while run:

    #drawing screen
    win.blit(bg, (0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((135, 206, 235))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()