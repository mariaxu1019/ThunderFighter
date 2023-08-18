
import sys

import pygame


from pygame.sprite import Group


from settings import Display_settings,Ship_settings,Bullet_settings,Trick_settings,Alien_settings,Sun_settings


from bullet import Bullet
from ship import Ship
from alien import Alien
from trick import Trick
from gamestats import GameStats
from botton import Botton
from scoreboard import Scoreboard

from sun import Sun
from chooser import Chooser

import functions 

def run_game():
    pygame.init()

 
    pygame.display.set_caption("植物大战僵尸雷霆战机版v0.1")


    ai_settings = Display_settings()

    ship_settings = Ship_settings()

    bullet_settings = Bullet_settings()

    trick_settings = Trick_settings()

    alien_settings = Alien_settings()

    sun_settings = Sun_settings()


    screen = pygame.display.set_mode(
        (ai_settings.width,ai_settings.height))
    

    stats = GameStats(ship_settings)
    

 
    scoreboard =Scoreboard(ai_settings,screen,stats)
    

    ship = Ship(screen,ship_settings,"Peashooter")

    suns = Group()


    chooser = Chooser(screen)

    

    bullets = Group()
    
    functions.creat_bullets(bullet_settings,bullets,screen,ship)
    

    #trick = Trick(screen)
    tricks = Group()


    aliens = Group()

    functions.create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats)

    play_botton = Botton(ai_settings,screen,"PLAY")
    
    

    while True:
        
        functions.check_events(ai_settings,screen,stats,play_botton,ship,tricks,suns,chooser)
        
        
        functions.play_botton(ai_settings,screen,stats,play_botton)
        
        
        if stats.game_active :
            
            functions.update_screen(
                
            ai_settings,

            screen,

            ship,ship_settings,

            bullets,bullet_settings,

            tricks,

            alien_settings,aliens,

            scoreboard,

            suns,sun_settings,
            
            stats,

            chooser
            )

            

            
            functions.collision(aliens,bullets,stats,alien_settings) 
            
                
            
            if functions.game_over(screen,ship,aliens) :
                functions.reborn(ai_settings,alien_settings,stats,screen,ship,aliens,bullets)




            

            
run_game()
