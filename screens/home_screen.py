import pygame


class playButton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def isClicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0] == 1
    
class HomeScreen:
    def __init__(self, screen, width=450, height=675):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg_image = pygame.image.load("assets/HomeScreenImage2.png")
        play_img = pygame.image.load("assets/playbutton3.png")
        self.play_button = playButton(120, 425, play_img)

    def draw(self):
        self.screen.blit(self.bg_image, (0,0))
        self.play_button.draw(self.screen)
    
    def handleEvent(self, mouse_pos, mouse_pressed, keys):
        if self.play_button.isClicked(mouse_pos, mouse_pressed) or keys[pygame.K_SPACE]:
            return "PLAYING"
        return "HOME"