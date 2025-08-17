import pygame, sys
from bird import Bird
pygame.init()

#setting up the game captions and fps
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

#setting up the dimensions of the window
width = 400
height = 675
win = pygame.display.set_mode((width,height))


#setting up the background
background = pygame.image.load("assets/backgroundfinal.png")
ground = pygame.image.load("assets/groundfinal.jpeg")
ground_scroll = 0
background_scroll = 0 #leaving now bug fix needed later
scroll_speed = 4

bird_group = pygame.sprite.Group()
flapper = Bird(200, int(height/2))
bird_group.add(flapper)

run = True
while run:
    
    #drawing screen and animating the moving background
    win.blit(background, (0,0))
    bird_group.draw(win)
    bird_group.update()
    win.blit(ground,(ground_scroll,474) )
    win.blit(ground,((ground_scroll + ground.get_width()),474))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 640:
        ground_scroll = 0




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()