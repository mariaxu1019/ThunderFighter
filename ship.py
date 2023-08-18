import pygame
class Ship():

    def __init__(self,screen,ship_settings,name):
   
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('resource\Plants\Peashooter.png')
        self.rect = self.image.get_rect()
        
        self.name = name

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.rect.bottom = self.screen_rect.bottom

  
        self.speed_factor = ship_settings.speed_factor

        self.ship_mv_rightflag = False
        self.ship_mv_leftflag = False
        self.ship_mv_upflag = False
        self.ship_mv_downflag = False
        

    def blitship(self):
    
        self.screen.blit(self.image,self.rect)

    def update_ship(self,ai_settings,ship_settings):
     
        if self.ship_mv_rightflag :
            if self.rect.centerx <= ai_settings.width:
                self.rect.centerx += ship_settings.speed_factor
        if self.ship_mv_leftflag :
            if self.rect.centerx >= ship_settings.speed_factor+1:
                self.rect.centerx -= ship_settings.speed_factor
        if self.ship_mv_downflag :             
            if self.rect.centery < ai_settings.height:                 
                self.rect.centery += ship_settings.speed_factor
        if self.ship_mv_upflag:
            if self.rect.centery > ship_settings.speed_factor+100:
                self.rect.centery -= ship_settings.speed_factor
    def center_ship(self):
        
        self.rect.centerx = self.screen_rect.centerx   
        self.rect.bottom = self.screen_rect.bottom
    def load_image(self,name):
       
        self.name = name
        if self.name == "Peashooter" :
            
            self.image = pygame.image.load('resource\Plants\Peashooter.png')
            self.speed_factor += 1 
            
        elif self.name == "SnowPea" :
          
            self.image = pygame.image.load('resource\Plants\SnowPea.png')
            self.speed_factor += 3
           
        elif self.name == "Threepeater" :
           
            self.image = pygame.image.load('resource\Plants\Peashooter.png')
            self.speed_factor += 5
            
        elif self.name == "Ironman" :
            
            self.image = pygame.image.load('resource\Plants\Ironman.png')
            self.speed_factor += 10

