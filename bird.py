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
        self.velocity = 0
        self.click = False

    def update(self, flying, game_over):

        keys = pygame.key.get_pressed()


        if flying == True:
            #bring the bird down
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 675:
                self.rect.y += int(self.velocity)

        if game_over == False:
            #control the bird to go up
            if (pygame.mouse.get_pressed()[0] == 1 or keys[pygame.K_SPACE]) and self.click == False:
                self.click = True
                self.velocity = -8
            if pygame.mouse.get_pressed()[0] == 0 and not keys[pygame.K_SPACE]:
                self.click = False


            self.counter += 1
            cooldown = 4

            if self.counter > cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
        
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

