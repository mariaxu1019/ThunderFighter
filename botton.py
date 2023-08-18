import pygame.font

class Botton():
    def __init__(self,ai_settings,screen,msg):
        
        self.screen = screen
        self.screen_rect = screen.get_rect()

        
        self.width =200
        self.height = 200 

        
        self.image = pygame.image.load('resource\Background\MainMenu.bmp')
        
        
        
        self.rect = pygame.Rect(0,0,1100,500)
        

        self.botton_color = (0,0,0)
        self.text_color = (120,120,120)
        self.font = pygame.font.SysFont(None,100)

        
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        
        self.msg_image = self.font.render(msg,False,self.text_color,self.botton_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        
        self.msg_image_rect.center = self.rect.center

    def draw_botton(self):
        
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

        
