import pygame

class resetButton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def isClicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0] == 1

class GameOverScreen:
    def __init__(self, screen, width=450, height=675):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg_image = pygame.image.load("assets/GameOver.png")
        gameover_img = pygame.image.load("assets/resetbutton3.png")
        self.restart_button = resetButton(125, 430, gameover_img)

    def draw(self, score):
        self.screen.blit(self.bg_image, (0,0))
        font = pygame.font.SysFont("Poppins", 40)
        text = font.render(f"Score: {score}", True, (0,0,255))
        self.screen.blit(text, (10, 10))
        self.restart_button.draw(self.screen)

    def handle_event(self, mouse_pos, mouse_pressed, keys):
        if self.restart_button.isClicked(mouse_pos, mouse_pressed) or keys[pygame.K_SPACE]:
            return "HOME"
        return "GAME_OVER"

