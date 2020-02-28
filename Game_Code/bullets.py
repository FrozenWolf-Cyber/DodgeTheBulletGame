import pygame
import math

WHITE = (255, 255, 255)

class bullet(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height , x ,y , angle,speed):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        pygame.draw.rect(self.image, color,  [0,0,width, height])
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.angle = angle

    def update(self):

        self.rect.x = self.rect.x + self.speed*math.cos(math.radians(self.angle))
        self.rect.y = self.rect.y + self.speed*math.sin(math.radians(self.angle))
        if self.rect.x >= 800 or self.rect.x<=0 or self.rect.y >=800 or self.rect.y<=0:
            self.kill()

    def destroy(self):
        self.kill()

    