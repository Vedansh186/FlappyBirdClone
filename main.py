import pygame, sys
from bird import Bird
from screens.home_screen import HomeScreen
from screens.game_over_screen import GameOverScreen
from pipe import Pipe
import random


pygame.init()
pygame.mixer.init()

#setting up the game captions and fps
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

#setting up the dimensions of the window
width = 450
height = 675
win = pygame.display.set_mode((width,height))
play_img = pygame.image.load("assets/playbutton3.png")
gameover_img = pygame.image.load("assets/resetbutton3.png")

#screens
home_screen = HomeScreen(win, play_img)
game_over_screen = GameOverScreen(win, gameover_img)
game_state = "HOME"

#setting up the background
background = pygame.image.load("assets/background2.png")
ground = pygame.image.load("assets/groundfinal.jpeg")

#setting up the variables
ground_scroll = 0
background_scroll = 0 #leaving now bug fix needed later
scroll_speed = 4
score = 0
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency

#setting up sounds
flap_sound = pygame.mixer.Sound("assets/flap.wav")
point_sound = pygame.mixer.Sound('assets/point.wav')
crash_sound = pygame.mixer.Sound('assets/crash.wav')

#calling bird class and making bird a sprite
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flapper = Bird(200, int(height/2), flap_sound)
bird_group.add(flapper)

run = True

#main game loop
while run:
    
    #mouse position corresponding to starting
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()


    #quit system and flying reset
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and flying == False and game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN or event.key == pygame.K_SPACE:
                flying = True

    #setting up home screen
    if game_state == "HOME":
        game_state = home_screen.handleEvent(mouse_pos, mouse_pressed, keys)
        home_screen.draw()

        #setting up playfield
        if game_state == "PLAYING":
            flying = True
            game_over = False
            flapper.rect.center = (200, int(height/2))
            flapper.velocity = 0
            score = 0
            pipe_group.empty()

    elif game_state == "PLAYING":
            #drawing screen
        win.blit(background, (0,0))

    #drawing the bird sprite and animating
        bird_group.draw(win)
        bird_group.update(flying, game_over)
        pipe_group.draw(win)
        pipe_group.update(scroll_speed)

        #setting up the scoring system
        for pipe in pipe_group:
            if not pipe.passed and pipe.rect.centerx < flapper.rect.centerx:
                pipe.passed = True
                score += 0.5
                point_sound.play()




    #drawing the ground
        win.blit(ground,(ground_scroll,474) )
        win.blit(ground,((ground_scroll + ground.get_width()),474))

    #collision detection
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flapper.rect.top < 0:
            game_over = True
            crash_sound.play()

    #animating the ground
        if game_over == False:
            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 640:
                ground_scroll = 0

    #checking to see if bird has hit the ground
        if flapper.rect.bottom > 474:
            game_over = True
            flying = False
            game_state = "GAME_OVER"
            crash_sound.play()


        #setting the spawning of pipes
        if game_over == False and flying == True:
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 50 )
                btm_pipe = Pipe(width, int(height / 2) + pipe_height, -1)
                top_pipe = Pipe(width, int(height / 2) + pipe_height, 1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now

    # Draw score
        font = pygame.font.SysFont("Poppins", 40)
        score_text = font.render(f"Score: {int(score)}", True, (0,255,0))
        win.blit(score_text, (10,10))
        
    
    elif game_state == "GAME_OVER":
        game_state = game_over_screen.handle_event(mouse_pos, mouse_pressed, keys)
        game_over_screen.draw(int(score))
        

        if game_state == "HOME":
            flying = False
            game_over = False
            flapper.rect.center = (200, int(height/2))
            flapper.velocity = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()