import pygame
YELLOW = (255, 242, 0)
WHITE = (255, 255, 255)
 
class boost(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height ,x , y ):

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
        
    def update(self):
       
        self.rect.x = self.rect.x+2

        if self.rect.x >= 800 or self.rect.x<=0 or self.rect.y >=800 or self.rect.y<=0:
            self.kill()

    def destroy(self):
        self.kill()


    