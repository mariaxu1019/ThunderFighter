import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,alien_settings,screen,name):

        
        super(Alien,self).__init__()
        
        self.screen = screen 
        
        self.name = name
        self.alien_settings = alien_settings
        self.speed_factor = alien_settings.x_speed

       
        self.image = pygame.image.load('resource\Zombies\Zombie.bmp')
        self.rect = self.image.get_rect()

        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height+50

        
        self.x = float(self.rect.x)

        self.load_image(name)
       

        

    def load_image(self,name):
        
        self.name = name
        if self.name == "Zombie" :
            self.image = pygame.image.load('resource\Zombies\Zombie.png')
        
        elif self.name == "BucketheadZombie"  :
            
            self.image = pygame.image.load('resource\Zombies\FlagZombie.png')
            self.speed_factor += 1 
            
        elif self.name == "ConeheadZombie" :
            
            self.image = pygame.image.load('resource\Zombies\ConeheadZombie.png')
            self.speed_factor += 2
           
        elif self.name == "FlagZombie" :
            
            self.image = pygame.image.load('resource\Zombies\\NewspaperZombie.png')
            self.speed_factor += 3

        elif self.name == "NewspaperZombie" :
            
            
            self.image = pygame.image.load('resource\Zombies\BucketheadZombie.png')
            self.speed_factor += 4

    def check_edges(self):
        
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True


    def update(self):
        
        self.x +=  (self.speed_factor*self.alien_settings.fleet_direction)
        self.rect.x = self.x


    





        


