import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,bullet_settings,screen,ship):
        

        super(Bullet,self).__init__()

        self.screen = screen

        self.bullet_settings = bullet_settings
        self.speed_factor = bullet_settings.speed_factor

        
        self.image = pygame.image.load('resource\Bullets\PeaNormal.png')
        self.rect = self.image.get_rect()

        
        self.rect.x = ship.rect.centerx
        self.rect.y = ship.rect.top

        
        self.y = float(ship.rect.y)

        self.load_image(ship)



    def load_image(self,ship):
        
        if ship.name == "Peashooter" :
            
            self.image = pygame.image.load('resource\Bullets\PeaNormal.png')
            self.speed_factor += 2 
            
        elif ship.name == "SnowPea" :
            
            self.image = pygame.image.load('resource\Bullets\PeaIce.png')
            self.speed_factor += 3
           
        elif ship.name == "Threepeater" :
            
            self.image = pygame.image.load('resource\Bullets\PeaNormalExplode.png')
            self.speed_factor += 5

        elif ship.name == "Ironman" :
            self.image = pygame.image.load('resource\Bullets\PalmCannon.png')
            self.speed_factor += 10
            

    def update(self):
        
        self.y -= self.speed_factor
        self.rect.y = self.y


        
        
        



        


