import pygame
from pygame.sprite import Sprite
import random
class Sun(Sprite):
 
    def __init__(self,sun_settings,screen):
        
        super(Sun,self).__init__()
        
        self.screen =screen
        self.image = pygame.image.load('resource\Background\Sun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

   
        self.sun_settings = sun_settings
        self.speed_factor = sun_settings.x_speed
        

        self.rect.centerx = random.randint(50,self.screen_rect.width)
        self.rect.centery = random.randint(50,self.screen_rect.height)

    
        self.x = float(self.rect.x)

    def blitsun(self):
     
        self.screen.blit(self.image,self.rect)

    def update(self):
       
        self.x +=  (self.speed_factor*self.sun_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
      
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

