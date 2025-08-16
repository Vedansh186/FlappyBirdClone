import pygame, sys
pygame.init()

width = 400
height = 600

win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


background = pygame.image.load("assets/bg.png")
pygame.display.set_caption("Flappy Bird")

run = True
while run:

    #drawing screen
    win.blit(background, (0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()