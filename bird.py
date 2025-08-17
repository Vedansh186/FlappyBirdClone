import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0

        for num in range(1,4):
            img = pygame.image.load(f'assets/bird{num}.png')
            self.images.append(img)

        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):

        self.counter += 1
        cooldown = 4

        if self.counter > cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        print(len(self.images))


