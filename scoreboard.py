import pygame.font

class Scoreboard():
 

    def __init__(self,ai_settings,screen,stats):
      
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

      
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,24)

      
        self.prep_scoreboard()

   
        self.prep_high_scoreboard()

       
        self.prep_level()

    
        self.prep_sun()

   
        self.prep_trick()


    def prep_scoreboard(self):
      
        score = "SCORE : "+"{:,}".format((self.stats.score))

        self.score_image = self.font.render(score,False,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right 

        self.score_rect.top   = self.screen_rect.top    


    def prep_high_scoreboard(self):
       
        high_score ="HIGH_SCORE : "+"{:,}".format((self.stats.high_score))

        self.high_score_image = self.font.render(high_score,False,self.text_color,self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.center = self.screen_rect.center

        self.high_score_rect.top   = self.screen_rect.top

    def prep_level(self):
        
        level = "LEVEL : "+"{:,}".format((self.stats.level))

        self.level_image = self.font.render(level,False,self.text_color,self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.screen_rect.right 

        self.level_rect.top   = self.screen_rect.top + 25  

    def prep_sun(self):
     

        sun = " "+ str(self.stats.sun_number) + " "

        self.sun_image = self.font.render(sun,False,self.text_color,self.ai_settings.bg_color)

        self.sun_rect = self.score_image.get_rect()

        self.sun_rect.left = self.screen_rect.left + 27

        self.sun_rect.top   = self.screen_rect.top + 64 

    def prep_ship_left(self):
       
        left = "LEFT : "+"{:,}".format((self.stats.ships_left))

        self.left_image = self.font.render(left,False,self.text_color,self.ai_settings.bg_color)

        self.left_rect = self.left_image.get_rect()

        self.left_rect.right = self.screen_rect.right 

        self.left_rect.top   = self.screen_rect.top   + 50


    def prep_trick(self):
    
        trick = "TRICK : "+"{:,}".format((self.stats.trick))

        self.trick_image = self.font.render(trick,False,self.text_color,self.ai_settings.bg_color)

        self.trick_rect = self.trick_image.get_rect()

        self.trick_rect.right = self.screen_rect.right 

        self.trick_rect.top   = self.screen_rect.top   + 75


    def draw_score(self):
   
        self.screen.blit(self.score_image,self.score_rect)

    def draw_high_score(self):
       
        self.screen.blit(self.high_score_image,self.high_score_rect)
    
    def draw_level(self):
    
        self.screen.blit(self.level_image,self.level_rect)

    def draw_sun(self):

        self.screen.blit(self.sun_image,self.sun_rect)

    def draw_ship_left(self):
 
        self.screen.blit(self.left_image,self.left_rect)

    def draw_trick(self):
    
        self.screen.blit(self.trick_image,self.trick_rect)


    
