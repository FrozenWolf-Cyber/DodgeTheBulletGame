
import pygame
WHITE = (255, 255, 255)
 
class Car(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height ,x , y):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width=width
        self.height=height
        self.color = color

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
    def update(self,keys):

        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - 5
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + 5
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - 5
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + 5

