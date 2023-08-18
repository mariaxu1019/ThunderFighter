import sys
import pygame
import time
from trick import Trick
from alien import Alien
from bullet import Bullet
from sun import Sun
from chooser import Chooser

       
       

def check_keydown_events(event,ship):
    
    if event.key == pygame.K_RIGHT:
        ship.ship_mv_rightflag = True 
    if event.key == pygame.K_LEFT:                              
        ship.ship_mv_leftflag = True
    if event.key == pygame.K_UP:                                              
        ship.ship_mv_upflag = True 
    if event.key == pygame.K_DOWN:
        ship.ship_mv_downflag = True 

def check_keyup_event(event,ship):
    
    if event.key == pygame.K_RIGHT:
        ship.ship_mv_rightflag=False
    if event.key == pygame.K_LEFT:
        ship.ship_mv_leftflag=False
    if event.key == pygame.K_UP:
        ship.ship_mv_upflag=False
    if event.key == pygame.K_DOWN:
        ship.ship_mv_downflag=False
      

def check_keyspace(event,tricks,screen,stats):
    
    if event.key  == pygame.K_SPACE:
        
        if stats.trick >= 1:
            trick = Trick(screen)
            tricks.add(trick)
            stats.trick_flag = True
        
def check_l(event,stats):
    
    if event.key == pygame.K_l:
        stats.ship = "Ironman"      
        

   
def check_click(area,mouse_x,mouse_y):
    
    print("area.rect.x=:{},area.rect.y=:{}.".format(area.rect.x,area.rect.y))
    if area.rect.collidepoint(mouse_x,mouse_y):
        return True

def check_clicksun(group,mouse_x,mouse_y):
    for member in group:
    
        print("member.rect.x=:{},member.rect.y=:{}.".format(member.rect.x,member.rect.y))
        if member.rect.collidepoint(mouse_x,mouse_y):
            return True
def check_clickitems(chooser,mouse_x,mouse_y):

    if chooser.card_cherrybomb_rect.collidepoint(mouse_x,mouse_y):
        return "Cherrybomb"

    elif chooser.card_snowpea_image_rect.collidepoint(mouse_x,mouse_y):
        return "SnowPea"

    elif chooser.card_threepeashooter_image_rect.collidepoint(mouse_x,mouse_y):
        return "Threepeashooter"
  



def check_events(ai_settings,screen,stats,play_botton,ship,tricks,suns,chooser):
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.K_q:
            sys.exit()
            

        elif event.type == pygame.MOUSEBUTTONDOWN : 
           
            mouse_x,mouse_y = pygame.mouse.get_pos()
            
            print("x=:{}，y=：{}".format(mouse_x,mouse_y))
            if check_click(play_botton,mouse_x,mouse_y):
                stats.game_active = True
                #stats.reset_stats()
                ship.center_ship()
                #game_start(stats,alien_settings,screen,aliens,alien_number,row_number,bullets)
            
            
            if check_clicksun(suns,mouse_x,mouse_y):
                stats.sun_number += 50
               
                for sun in suns.copy(): 
                    suns.remove(sun)

            if check_clickitems(chooser,mouse_x,mouse_y) == "Cherrybomb":
                if stats.sun_number >= 150:
                    stats.sun_number -=150
                    stats.trick += 1

            if check_clickitems(chooser,mouse_x,mouse_y) == "SnowPea":
                if stats.sun_number >= 175:
                    stats.sun_number -=175 
                    stats.ship = "SnowPea"

            if check_clickitems(chooser,mouse_x,mouse_y) == "Threepeashooter":
                if stats.sun_number >= 300:
                    stats.sun_number -= 300
                    stats.ship = "Threepeashooter"

            
            
        elif event.type==pygame.KEYDOWN:
       
            check_keydown_events(event,ship)

            check_keyspace(event,tricks,screen,stats)

            check_l(event,stats)

 
        elif event.type==pygame.KEYUP:
         
            check_keyup_event(event,ship)
         



 
                     
def delete_member(group):
         """ 删除离开屏幕的编组元素，释放内存"""     
         for member in group.copy():         
             if member.rect.bottom <= 0 :             
                 group.remove(member)



def get_number_alines_x(ai_settings,alien_width):

    avaliable_space_x = ai_settings.width - 2*alien_width

    number_aliens_x = int(avaliable_space_x / (2*alien_width))

    return number_aliens_x


def get_number_aliens_y(ai_settings,ship_height,alien_height):

    avaliable_space_y=( ai_settings.height - (2*alien_height) - ship_height)

    number_aliens_y = int (avaliable_space_y / (3*alien_height) )

    return number_aliens_y
                   
def create_aliens(alien_settings,screen,aliens,alien_number,row_number,stats):

    alien = Alien(alien_settings,screen,"Zombie")

    if stats.level == 2:
        alien.load_image("BucketheadZombie")  
    elif stats.level == 3:
        alien.load_image("ConeheadZombie")
    elif stats.level == 4:
        alien.load_image("FlagZombie")
    elif stats.level == 5:
        alien.load_image("NewspaperZombie")
        
    
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x


    alien_height = alien.rect.height
    

    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y

    aliens.add(alien)



def create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats):

    
    
    alien_settings.increase_speed()
    alien = Alien(alien_settings,screen,"Zombie")


    number_aliens_x = get_number_alines_x(ai_settings, alien.rect.width)
    print(number_aliens_x)

    number_aliens_y = get_number_aliens_y(ai_settings, ship.rect.height, alien.rect.height)
    print(number_aliens_y)


    for row_number in range(number_aliens_y):
  
        for alien_number in range(number_aliens_x):
            create_aliens(alien_settings,screen,aliens,alien_number,row_number,stats)


def change_direction(settings,group):

    for member in group.sprites():
        #alien.y += alien_settings.y_speed
        member.rect.y += settings.y_speed
    settings.fleet_direction *= -1

def check_edges(settings,group):

    for member in group.sprites():
        if member.check_edges():
            change_direction(settings,group)
            break

def creat_bullets(bullet_settings,bullets,screen,ship):

    bullet = Bullet(bullet_settings,screen,ship)

    bullets.add(bullet)



def creat_trick(tricks,screen):
  
    trick = Trick(screen)
    
    tricks.add(trick)


def creat_suns(sun_settings, suns, screen):

    sun = Sun(sun_settings, screen)
    suns.add(sun)


def check_high_score(stats):

    if stats.score > stats.high_score :
        stats.high_score = stats.score

def collision(First,Second,stats,alien_settings):

    collisions = pygame.sprite.groupcollide(First,Second,True,True)

    if collisions :
        for aliens in collisions.values() :
            stats.score += alien_settings.point * len(aliens)
        check_high_score(stats)  




def game_over(screen,ship,aliens):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            return True
    if pygame.sprite.spritecollideany(ship,aliens):
        print("GAME OVER!")
        return True




def reborn(ai_settings,alien_settings,stats,screen,ship,aliens,bullets):

    if stats.ships_left >0 :
        stats.ships_left -= 1
    else :
        stats.game_active = False

    aliens.empty()
    bullets.empty()

    alien_settings.initialize_dynamic_settings()
    create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats)
    ship.center_ship()


    time.sleep(0.5)

def play_botton(ai_settings,screen,stats,play_botton):
    if not stats.game_active :

        play_botton.draw_botton()
  
        pygame.display.flip()

def update_trick(tricks,screen,stats,aliens):

    def delet(tricks,stats):
        for trick in tricks.copy():
            tricks.remove(trick)

 
    def delet_fleet(aliens,stats):
        for alien in aliens.copy():
            stats.score += 50
            aliens.remove(alien)
    

    def blit(tricks,screen,stats,aliens):
        starttime=time.time()
        if stats.trick_flag :

            if len(tricks) >= 1:
        
                tricks.draw(screen)
                pygame.display.flip()
                time.sleep(1.0 - ((time.time() - starttime) % 1.0))
                delet_fleet(aliens,stats)
                stats.trick -= 1
                stats.trick_flag = False 
        

    blit(tricks,screen,stats,aliens)
    delet(tricks,stats)

def update_ship(ai_settings,ship_settings,ship,stats): 
    if stats.ship == "SnowPea"  :
        ship.load_image("SnowPea")

    elif stats.ship == "Repeaterpea"  :
        ship.load_image("Repeaterpea")

    elif stats.ship == "Threepeashooter"  :
        ship.load_image("Threepeater")

    elif stats.ship == "Ironman" :
        ship.load_image("Ironman")

    ship.blitship()
  
    ship.update_ship(ai_settings,ship_settings)


def update_sun(sun_settings,suns,screen):

    check_edges(sun_settings,suns)
    suns.update()
    if len(suns) == 0:
        creat_suns(sun_settings,suns,screen)


    suns.draw(screen)

  
    delete_member(suns)


def update_bullets(bullet_settings,bullets,screen,ship):
    

    if len(bullets) == 0:
        creat_bullets(bullet_settings,bullets,screen,ship)
    
    
    bullets.update()

    delete_member(bullets)

    bullets.draw(screen)


def update_aliens(ai_settings,alien_settings,screen,ship,aliens,stats):

    check_edges(alien_settings,aliens)
    aliens.update()
    if len(aliens) == 0:
        create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats)

    aliens.draw(screen)

def update_imformation(chooser,scoreboard):

    chooser.blitchooser()
    chooser.blitchooser_items()

    scoreboard.prep_scoreboard()
    scoreboard.draw_score()
    
    scoreboard.prep_scoreboard()
    scoreboard.draw_high_score()

    scoreboard.prep_level()
    scoreboard.draw_level()

    scoreboard.prep_sun()
    scoreboard.draw_sun()

    scoreboard.prep_ship_left()
    scoreboard.draw_ship_left()

    scoreboard.prep_trick()
    scoreboard.draw_trick()

def update_screen(
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
    ):

    screen.blit(ai_settings.image,ai_settings.rect)

    stats.check_high_score()
    stats.check_level()

    update_trick(tricks,screen,stats,aliens)

    update_ship(ai_settings,ship_settings,ship,stats)

    update_sun(sun_settings,suns,screen)

    update_bullets(bullet_settings,bullets,screen,ship)

    update_aliens(ai_settings,alien_settings,screen,ship,aliens,stats)

    update_imformation(chooser,scoreboard)
 
    pygame.display.flip()
