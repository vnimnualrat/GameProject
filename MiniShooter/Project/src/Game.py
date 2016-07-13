'''
Created on May 4, 2015

@author: LittleMonster
'''
import pygame, sys
from pygame.locals import *
from player import Player
from bullet import Bullet
from cow import Cow
from player2 import Player2
from player3 import Player3
from ammo import Ammo
from ammofloat import AmmoFloat
from horseshoe import HorseShoe
from skull import Skull
from dynamite import Dynamite
from star import Star
from tnt import Tnt
import random
import pygame.time

#These were the bottom floating object that were originally moving left.
def move_floating_objects_bottom(floating_objects_list_left):
    """
    Args: 
        floating_objects_list_left(sprite group): The sprite group that is
        moving across the screen on the bottom.
    Yields:
        sprite group: Moves all the sprite objects that was added to the sprite
        group.
    """
    for i in floating_objects_list_left:
        i.rect.x -= 1
        if i.rect.x < 0:
            i.rect.x = 1000
            i.rect.x -= 1
    
#These are the top moving objects that were originally moving right.
def move_floating_objects_top(floating_objects_list_right):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the top.
    Yields:
        sprite group: Moves all the sprite objects that was added to the sprite
        group.
    """
    for i in floating_objects_list_right:
        i.rect.x += 1
        if i.rect.x > 900:
            i.rect.x = -1
            i.rect.x += 1

#Moves floating objects to the right.
def load_floating_objects_top(floating_objects_list_top, all_sprites_list):
    """
    Args: 
        floating_objects_list_top(sprite group): The sprite group that is
        moving across the screen on the top.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
    Yields:
        sprite group: Loads all the sprite objects that was added to the sprite
        group.
    """
    for i in floating_objects_list_top:
        all_sprites_list.add(i)

#Moves floating objects to the left        
def load_floating_objects_bottom(floating_objects_list_bottom, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
    Yields:
        sprite group: Loads all the sprite objects that was added to the sprite
        group.
    """
    for i in floating_objects_list_bottom:
        all_sprites_list.add(i)


def load_skull_bottom(floating_objects_list_bottom, skull_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        skull_sprite_group(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
    Yields:
        sprite group: Loads the skull to the list to be detected by collision
        for points.
    """
    for i in range(1):
        skull = Skull()
        if i == 0: #1st object
            skull.rect.x = 0
            skull.rect.y = 130
        floating_objects_list_bottom.add(skull)
        skull_sprite_list.add(skull)

def load_tnt_bottom(floating_objects_list_bottom, tnt_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        tnt_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the tnt to the list to be detected by collision
        for points.
    """
    for i in range(2):
        tnt = Tnt()
        if i == 0: #2nd object
            tnt.rect.x = 120
            tnt.rect.y = 135
        if i == 1: #8th object in the list
            tnt.rect.x = 840
            tnt.rect.y = 130
        floating_objects_list_bottom.add(tnt)
        tnt_sprite_list.add(tnt)
        
#Bottom ammo moving object
def load_ammo_object_bottom(floating_objects_list_bottom, ammofloat_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        ammofloat_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the ammo to the list to be detected by collision
        for automatic ammo reload.
    """
    for i in range(1):
        theammo = AmmoFloat()
        if i == 0: #3rd object
            theammo.rect.x = 240
            theammo.rect.y = 130
        floating_objects_list_bottom.add(theammo)
        ammofloat_sprite_list.add(theammo)

def load_cow_bottom(floating_objects_list_bottom, cow_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        cow_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the cow to the list to be detected by collision
        for points.
    """
    for i in range(2):
        cow = Cow()
        if i == 0: #4th object
            cow.rect.x = 360
            cow.rect.y = 130
        if i == 1:
            cow.rect.x = 720
            cow.rect.y = 130
        floating_objects_list_bottom.add(cow)
        cow_sprite_list.add(cow)

def load_star_bottom(floating_objects_list_bottom, star_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        star_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the star to the list to be detected by collision
        for increased bullet speed
    """
    for i in range(1):
        star = Star()
        if i == 0: #5th object
            star.rect.x = 480
            star.rect.y = 130
            floating_objects_list_bottom.add(star)
            star_sprite_list.add(star)
            
def load_horseshoe_bottom(floating_objects_list_bottom, horseshoe_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_bottom(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        horseshoe_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the star to the list to be detected by collision
        for points.
    """
    for i in range(1):
        horseshoe = HorseShoe()
        if i == 0: #6th object
            horseshoe.rect.x = 599
            horseshoe.rect.y = 135
        floating_objects_list_bottom.add(horseshoe)
        horseshoe_sprite_list.add(horseshoe)

def load_CowObject_top(floating_objects_list_right, cow_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        cow_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the cows to the list to be detected by collision
        for points.
    """
    for i in range(2):
        cow = Cow()
        if i == 0: #1st object
            cow.rect.x = -1
            cow.rect.y = 60
        if i == 1: #7th
            cow.rect.x = -580
            cow.rect.y = 60
        floating_objects_list_right.add(cow)
        cow_sprite_list.add(cow)

def load_HorseShoe_top(floating_objects_list_right, horseshoe_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        horseshoe_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the horse shoes to the list to be detected by collision
        for points.
    """
    for i in range(1):
        horseshoe = HorseShoe()
        if i == 0: #2nd object
            horseshoe.rect.x = -120
            horseshoe.rect.y = 60
        floating_objects_list_right.add(horseshoe)
        horseshoe_sprite_list.add(horseshoe) 
    
def load_dynamite_top(floating_objects_list_right, dynamite_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        dynamite_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the dynamites to the list to be detected by collision
        for points.
    """
    for i in range(1):
        dynamite = Dynamite()
        if i == 0: #4th object
            dynamite.rect.x = -240
            dynamite.rect.y = 60
        floating_objects_list_right.add(dynamite)
        dynamite_sprite_list.add(dynamite)
        
# RIGHT MOVING AMMO OBJECT
def load_AmmoObject_top(floating_objects_list_right, ammofloat_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        ammofloat_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the ammo to the list to be detected by collision
        for automatic ammo reload.
    """
    for i in range(2):
        ammofloat = AmmoFloat()
        if i == 0: #5th object
            ammofloat.rect.x = -340
            ammofloat.rect.y = 60
        if i == 1: #9th object
            ammofloat.rect.x = -805
            ammofloat.rect.y = 60
        floating_objects_list_right.add(ammofloat)
        ammofloat_sprite_list.add(ammofloat)        

def load_star_top(floating_objects_list_top, star_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        star_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the star to the list to be detected by collision
        for increased bullet speed.
    """
    for i in range(1):
        star = Star()
        if i == 0: #6th object
            star.rect.x = -460
            star.rect.y = 60
        floating_objects_list_top.add(star)
        star_sprite_list.add(star)
        
def load_skull_top(floating_objects_list_top, skull_sprite_list, all_sprites_list):
    """
    Args: 
        floating_objects_list_right(sprite group): The sprite group that is
        moving across the screen on the bottom.
        
        skull_sprite_list(sprite group): Sprite group used to detect
        collision in order to add points to the player's score.
        
        all_sprite_list(sprite group): The sprite group that contains all 
        sprites to be displayed.
        
    Yields:
        sprite group: Loads the skull to the list to be detected by collision
        for points.
    """
    for i in range(1):
        skull = Skull()
        if i == 0: #8th object
            skull.rect.x = -700
            skull.rect.y = 60
        floating_objects_list_top.add(skull)
        skull_sprite_list.add(skull)

        
def automoveplayer2(player2, counterp2):
    """
    Args: 
        player2(Player): Takes the player to determine player movement.
        
        counterp2(int): Determines when the player moves left or right with 
        the help of a random number generator.
        
    Yields:
        player: Movement left or right
    """
    randNum = random.randint(0,10)
    if (counterp2/2) % 2 == 0:
        if randNum == 2:
            player2.moveLeft(1)
        else:
            player2.moveRight(1.5)
    if (counterp2/2) % 2 == 1:
        if randNum == 3:
            player2.moveRight(1)
        else:
            player2.moveLeft(1.5)

def automoveplayer3(player3, counterp3):
    """
    Args: 
        player3(Player): Takes the player to determine player movement.
        
        counterp3(int): Determines when the player moves left or right with 
        the help of a random number generator.
        
    Yields:
        player: Movement left or right
    """
    randNum = random.randint(0,10)
    if (counterp3/2) % 2 == 0:
        if randNum == 0:
            player3.moveLeft(1)
        else:
            player3.moveRight(1.5)
    if (counterp3/2) % 2 == 1:
        if randNum == 0:
            player3.moveRight(1)
        else:
            player3.moveLeft(1.5)

def locationplayer1(player):
    player.rect.y = 280
    
def locationplayer2(player2):
    player2.rect.y = 280
    player2.rect.x = 380
    
def locationplayer3(player3):
    player3.rect.y = 280
    player3.rect.x = 800
    
def main():
    pygame.init()

    ak47_sound = pygame.mixer.Sound('sounds/ak47-1.ogg')
    ak_reload3 = pygame.mixer.Sound('sounds/ak47_boltpull.ogg')
    empty_pistolsound = pygame.mixer.Sound('sounds/clipempty_pistol.ogg')
    LetItGo = pygame.mixer.Sound('sounds/LetItGo.ogg')
    moosound = pygame.mixer.Sound('sounds/moosound.ogg')
    starsound = pygame.mixer.Sound('sounds/Ding.ogg')
    
    bg_p1won = pygame.image.load('images/winner.png')
    bg_p2won = pygame.image.load('images/loserkeenanwon.png')
    bg_p3won = pygame.image.load('images/loserkeenan2.0.png')
    bg = pygame.image.load('images/WesternBackgroundTest2.png')
    
    size = width, height = 1000, 500
    screen = pygame.display.set_mode(size)
    
    #Creates all sprite group.
    all_sprites_list = pygame.sprite.Group()
    
    # Bullet for Player 1
    bullet_list = pygame.sprite.Group()
    
    # Bullet for Player 2
    bullet_list2 = pygame.sprite.Group()
    
    # Bullet for Player 3
    bullet_list3 = pygame.sprite.Group()
    
    # Cow sprite list
    cow_sprite_list = pygame.sprite.Group()
    
    # Horseshoe sprite list
    horseshoe_sprite_list = pygame.sprite.Group()
    
    # Skull sprite list
    skull_sprite_list = pygame.sprite.Group()
    
    # Ammofloat sprite list
    ammofloat_sprite_list = pygame.sprite.Group()
    
    # Star sprite list
    star_sprite_list = pygame.sprite.Group()
    
    # Tnt sprite list
    tnt_sprite_list = pygame.sprite.Group()
    
    # Dynamite sprite list
    dynamite_sprite_list = pygame.sprite.Group()
    
    # Floating objects moving top
    floating_objects_list_top = pygame.sprite.Group()
    
    # Floating objects moving bottom
    floating_objects_list_bottom = pygame.sprite.Group()
    
    'Boolean to determine whether they hit a star. If they hit a star, bullet speed increases.'
    hit = False
    hitp2 = False
    hitp3 = False
    
    'Boolean to determine if someone has won the game.'
    p1won = False
    p2won = False
    p3won = False
    
    'Boolean that checks whether or not the game is over and to display a winning condition'
    gameOver = False
    
    LetItGo.play()
    
    'Loads all the floating objects on the top that are moving.'
    load_HorseShoe_top(floating_objects_list_top, horseshoe_sprite_list, 
                       all_sprites_list)
    
    load_AmmoObject_top(floating_objects_list_top, ammofloat_sprite_list, 
                        all_sprites_list)
    
    load_CowObject_top(floating_objects_list_top, cow_sprite_list, 
                       all_sprites_list)
    
    load_star_top(floating_objects_list_top, star_sprite_list, 
                  all_sprites_list)
    
    load_dynamite_top(floating_objects_list_top, dynamite_sprite_list, 
                      all_sprites_list)
    
    load_skull_top(floating_objects_list_top, skull_sprite_list, 
                   all_sprites_list)
    
    
    'Loads all the floating objects on the bottom that are moving.'
    load_ammo_object_bottom(floating_objects_list_bottom, ammofloat_sprite_list, 
                            all_sprites_list)
    
    load_skull_bottom(floating_objects_list_bottom, skull_sprite_list, 
                      all_sprites_list)
    
    load_tnt_bottom(floating_objects_list_bottom, tnt_sprite_list, 
                    all_sprites_list)
    
    load_cow_bottom(floating_objects_list_bottom, cow_sprite_list, 
                    all_sprites_list)
    
    load_star_bottom(floating_objects_list_bottom, star_sprite_list, 
                     all_sprites_list)
    
    load_horseshoe_bottom(floating_objects_list_bottom, horseshoe_sprite_list, 
                          all_sprites_list)
    
    'Puts all the floating objects on the top into a single list.'
    load_floating_objects_top(floating_objects_list_top, all_sprites_list)
    
    'Puts all the floating objects on the bottom into a single list.'
    load_floating_objects_bottom(floating_objects_list_bottom, all_sprites_list)
    
    starlist = []
    starlist2 = []
    starlist3 = []
    
    'Creates an ammo sprite group for player 1. This determines the amount of bullet the player starts with.'
    ammolist = []
    ammo_list = pygame.sprite.Group()
    for i in range(6):
        oh = Ammo()
        oh.rect.x = 30 + i*15
        oh.rect.y = 450
        ammolist.append(oh)
        ammo_list.add(oh)
        all_sprites_list.add(oh)
    
    'Creates an ammo sprite group for player 2. This determines the amount of bullet the player starts with.'
    ammolist2 = []
    ammo_list2 = pygame.sprite.Group()
    for i in range(6):
        ammo2 = Ammo()
        ammo2.rect.x = 350 + i*15
        ammo2.rect.y = 450
        ammolist2.append(ammo2)
        ammo_list2.add(ammo2)
        all_sprites_list.add(ammo2)
        
    'Creates an ammo sprite group for player 3. This determines the amount of bullet the player starts with.'
    ammolist3 = []
    ammo_list3 = pygame.sprite.Group()
    for i in range(6):
        ammo3 = Ammo()
        ammo3.rect.x = 730 + i*15
        ammo3.rect.y = 450
        ammolist3.append(ammo3)
        ammo_list3.add(ammo3)
        all_sprites_list.add(ammo3)
    
    'Instantiate the players.'
    player = Player()
    player2 = Player2()
    player3 = Player3()
    
    'Add the players to the all sprites group.'
    all_sprites_list.add(player)
    all_sprites_list.add(player2)
    all_sprites_list.add(player3)
    
    'Set default location of players.'
    locationplayer1(player)
    locationplayer2(player2)
    locationplayer3(player3)
    
    'This updates the score for each player after hitting a sprite.'
    p1score = 0
    p2score = 0
    p3score = 0
    
    'This counter helps determine the movement of the computer'
    counterp2 = 0
    counterp3 = 0

    'Sets up the default scoresheet when the game starts'
    gamefont = pygame.font.FontType('Furmanite Bold.ttf', 30)
    scoretext = gamefont.render('SquirtYay: ' + str(p1score), 2, [255,0,0])
    scoretext2 = gamefont.render('Keenan: ' + str(p2score), 2, [255, 255, 255])
    scoretext3 = gamefont.render('Keenan 2.0: '+ str(p3score), 2, [37, 171, 27])
    boxsize = scoretext.get_rect()
    boxsize2 = scoretext2.get_rect()
    boxsize3 = scoretext3.get_rect()
    scoreXpos = (450-boxsize[2])/2
    scoreXpos2 = (550-boxsize2[2]/2)
    scoreXpos3 = (800-boxsize3[2]/2)
    
    'Determines the time for when player 2 will shoot a bullet.'
    time_elapsed_since_last_action = 0
    
    'Determines the time for when player 3 will shoot a bullet.'
    time_elapsed_since_last_action2 = 0
    
    'Creates an object to help track time.'
    clock = pygame.time.Clock()
    
    while True:  # <--- main game loop
        'Blit the background onto the screen.'
        screen.blit(bg, (0,0))
        
        'This updates the score board every time an object is shot at.'
        scoretext = gamefont.render('SquirtYay: ' + str(p1score), 2, [255,0,0])
        scoretext2 = gamefont.render('Keenan: '+str(p2score), 2, [255, 255, 255])
        scoretext3 = gamefont.render('Keenan 2.0: '+str(p3score), 2, [37,171,27])
        screen.blit(scoretext, [scoreXpos, 20])
        screen.blit(scoretext2, [scoreXpos2, 20])
        screen.blit(scoretext3, [scoreXpos3, 20])
        
        'Increase the time while game is on.'
        dt = clock.tick()
        time_elapsed_since_last_action += dt
        time_elapsed_since_last_action2 += dt
        
        'If the game is over display the winning background.'
        while gameOver == True:
            if p1won == True:
                screen.blit(bg_p1won, (0,0))
            if p2won == True:
                screen.blit(bg_p2won, (0,0))
            if p3won == True:
                screen.blit(bg_p3won, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and len(ammolist) > 0 and gameOver == False:
                'Fire a bullet if the user clicks the mouse button'
                bullet = Bullet()
                ak47_sound.play()
                
                'Removes ammunition from the list and screen every time the player shoots'
                if len(ammolist) > 0:
                    newList = ammolist.pop()
                    all_sprites_list.remove(newList)
                    
                'Set the bullet so it is where the player is'
                bullet.rect.x = player.rect.x+65
                bullet.rect.y = player.rect.y+10
                
                'Adds the bullet to the lists'
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)               
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                        for i in range(6):
                            all_sprites_list.remove(ammolist)
                        ammolist.clear()
                        for i in range(6):
                            oh = Ammo()
                            oh.rect.x = 30 + i*15
                            oh.rect.y = 450
                            ammolist.append(oh)
                            ammo_list.add(oh)
                            all_sprites_list.add(oh)
                        ak_reload3.play()
            elif event.type == pygame.MOUSEBUTTONDOWN and len(ammolist) == 0:
                empty_pistolsound.play()
                
        'This checks for the winning conditions. If someone has won, it will set the game over and whoever won to true. Ending the game.'
        if p1score >= 70:
            gameOver = True
            p1won = True
        if p2score >= 70:
            gameOver = True
            p2won = True   
        if p3score >= 70:
            gameOver = True
            p3won = True
            
        'PLAYER 2 ACTIONS'
        'Wait until begin shooting.'
        if time_elapsed_since_last_action > 950:
            #player 2's Bullet
            bullet2 = Bullet()
            ak47_sound.play()
            bullet2.rect.x = player2.rect.x + 61
            bullet2.rect.y = player2.rect.y + 10
            'Each time the player shoots an ammo and it is greater than 0. Remove one from the display list.'
            if len(ammolist2) > 0:
                    newList2 = ammolist2.pop()
                    all_sprites_list.remove(newList2)
                    'This counter is incremented every time the player shoots to determine when the player will move. '
                    counterp2 += 1
            ' If the player no longer has ammo. Automatically reload the list. '
            if len(ammolist2) == 0:
                empty_pistolsound.play()
                ak_reload3.play()
                for i in range(6):
                    ammo2 = Ammo()
                    ammo2.rect.x = 350 + i*15
                    ammo2.rect.y = 450
                    ammolist2.append(ammo2)
                    ammo_list2.add(ammo2)
                    all_sprites_list.add(ammo2)
            all_sprites_list.add(bullet2)
            bullet_list2.add(bullet2)
            time_elapsed_since_last_action = 0
            
                
        #automoveplayer2
        automoveplayer2(player2, counterp2)

        'Player 3 ACTIONS'
        if time_elapsed_since_last_action2 > 1200:
            #player 2's Bullet
            bullet3 = Bullet()
            ak47_sound.play()
            bullet3.rect.x = player3.rect.x + 60
            bullet3.rect.y = player3.rect.y + 10
            
            # Removes AMMO from list
            if len(ammolist3) > 0:
                    newList3 = ammolist3.pop()
                    all_sprites_list.remove(newList3)
                    #counter to move player
                    counterp3 += 1
                    #print(counterp3)
            if len(ammolist3) == 0:
                empty_pistolsound.play()
                ak_reload3.play()
                for i in range(6):
                    ammo3 = Ammo()
                    ammo3.rect.x = 730 + i*15
                    ammo3.rect.y = 450
                    ammolist3.append(ammo3)
                    ammo_list3.add(ammo3)
                    all_sprites_list.add(ammo3)
            all_sprites_list.add(bullet3)
            bullet_list3.add(bullet3)
            time_elapsed_since_last_action2 = 0
            
        'automoveplayer3'
        automoveplayer3(player3, counterp3)
            
        
        'Player 1 sprite collision'
        for bullet in bullet_list:
            cow_hit_list = pygame.sprite.spritecollide(bullet, 
                                                       cow_sprite_list, True)
            
            horseshoe_hit_list = pygame.sprite.spritecollide(bullet,
                                                    horseshoe_sprite_list, True)
            
            ammo_hit_list = pygame.sprite.spritecollide(bullet,
                                                    ammofloat_sprite_list, True)
            
            skull_hit_list = pygame.sprite.spritecollide(bullet, 
                                                    skull_sprite_list, True)
            tnt_hit_list = pygame.sprite.spritecollide(bullet, 
                                                    tnt_sprite_list, True)
            star_hit_list = pygame.sprite.spritecollide(bullet, 
                                                    star_sprite_list, True)
            dynamite_hit_list = pygame.sprite.spritecollide(bullet, 
                                                    dynamite_sprite_list, True)
            if hit == False:
                bullet.bulletspeed(3)
            else:
                bullet.bulletspeed(7)
            'If the player hits an ammo, it will automatically reload their bullets.'
            for ammofloat in ammo_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                ak_reload3.play()
                for i in range(6):
                    all_sprites_list.remove(ammolist)
                    ammolist.clear()
                for i in range(6):
                    oh = Ammo()
                    oh.rect.x = 50 + i*15
                    oh.rect.y = 450
                    ammolist.append(oh)
                    ammo_list.add(oh)
                    all_sprites_list.add(oh)
            for horseshoe in horseshoe_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                p1score += 3
            for cow in cow_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                p1score += 3
                moosound.play()
            ' If the player hits a skull, it will remove the bullets of the other players forcing them to reload.'
            for skull in skull_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                for i in range(6):
                    all_sprites_list.remove(ammolist2)
                    ammolist2.clear()
                for i in range(6):
                    all_sprites_list.remove(ammolist3)
                    ammolist3.clear()
            for tnt in tnt_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                p1score += 5
            for star in star_hit_list:
                starsound.play()
                hit = True
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                star_obj = Star()
                star_obj.rect.x = 245
                star_obj.rect.y = 440
                starlist.append(star_obj)
                star_sprite_list.add(starlist)
                all_sprites_list.add(starlist)
            for dynamite in dynamite_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                p1score += 5  
                      
        'Player 2 sprite collision'
        for bullet2 in bullet_list2:
            cow_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                       cow_sprite_list, True)
            
            horseshoe_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                    horseshoe_sprite_list, True)
            
            ammo_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                    ammofloat_sprite_list, True)
            
            skull_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                    skull_sprite_list, True)
            
            tnt_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                       tnt_sprite_list, True)
            
            star_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                    star_sprite_list, True)
            
            dynamite_hit_list = pygame.sprite.spritecollide(bullet2, 
                                                    dynamite_sprite_list, True)
            if hitp2 == False:
                bullet2.bulletspeed(3)
            else:
                bullet2.bulletspeed(7)
            ' If the player hits an ammo, it will automatically reload their bullets.'
            for ammofloat in ammo_hit_list:
                bullet_list2.remove(bullet2)
                all_sprites_list.remove(bullet2)
                ak_reload3.play()
                for i in range(6):
                    all_sprites_list.remove(ammolist2)
                    ammolist2.clear()
                for i in range(6):
                    ammo2 = Ammo()
                    ammo2.rect.x = 350 + i*15
                    ammo2.rect.y = 450
                    ammolist2.append(ammo2)
                    ammo_list2.add(ammo2)
                    all_sprites_list.add(ammo2)
            for  horseshoe in horseshoe_hit_list:
                bullet_list2.remove(bullet2)
                all_sprites_list.remove(bullet2)
                p2score += 3
            for cow in cow_hit_list:
                bullet_list2.remove(bullet2)
                all_sprites_list.remove(bullet2)
                p2score += 3
                moosound.play()
            ' If the player hits a skull, it will remove the bullets of the other players forcing them to reload.'
            for skull in skull_hit_list:
                bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
                for i in range(6):
                    all_sprites_list.remove(ammolist)
                    ammolist.clear()
                for i in range(6):
                    all_sprites_list.remove(ammolist3)
                    ammolist3.clear()
            for tnt in tnt_hit_list:
                bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
                p2score += 5
            for star in star_hit_list:
                starsound.play()
                hitp2 = True
                bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
                star_obj = Star()
                star_obj.rect.x = 600
                star_obj.rect.y = 440
                starlist2.append(star_obj)
                star_sprite_list.add(starlist2)
                all_sprites_list.add(starlist2)
            for dynamite in dynamite_hit_list:
                bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
                p2score += 5
                
        'Player 3 sprite collision'
        for bullet3 in bullet_list3:
            cow_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                cow_sprite_list, True)
            
            horseshoe_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                    horseshoe_sprite_list, True)
            
            ammo_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                    ammofloat_sprite_list, True)
            
            skull_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                    skull_sprite_list, True)
            
            tnt_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                    tnt_sprite_list, True)
            
            star_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                    star_sprite_list, True)
            
            dynamite_hit_list = pygame.sprite.spritecollide(bullet3, 
                                                    dynamite_sprite_list, True)
            if hitp3 == False:
                bullet3.bulletspeed(6)
            else:
                bullet3.bulletspeed(10)
            ' If the player hits an ammo, it will automatically reload their bullets.'
            for ammofloat in ammo_hit_list:
                bullet_list3.remove(bullet3)
                all_sprites_list.remove(bullet3)
                ak_reload3.play()
                for i in range(6):
                    all_sprites_list.remove(ammolist3)
                    ammolist3.clear()
                for i in range(6):
                    ammo3 = Ammo()
                    ammo3.rect.x = 715 + i*15
                    ammo3.rect.y = 450
                    ammolist3.append(ammo3)
                    ammo_list3.add(ammo3)
                    all_sprites_list.add(ammo3)
            for  horseshoe in horseshoe_hit_list:
                bullet_list3.remove(bullet3)
                all_sprites_list.remove(bullet3)
                p3score += 3
            for cow in cow_hit_list:
                bullet_list3.remove(bullet3)
                all_sprites_list.remove(bullet3)
                p3score += 3
                moosound.play()
            'If the player hits a skull, it will remove the bullets of '
            'the other players forcing them to reload.'
            for skull in skull_hit_list:
                bullet_list.remove(bullet2)
                all_sprites_list.remove(bullet2)
                for i in range(6):
                    all_sprites_list.remove(ammolist)
                    ammolist.clear()
                for i in range(6):
                    all_sprites_list.remove(ammolist2)
                    ammolist2.clear()
            for tnt in tnt_hit_list:
                bullet_list.remove(bullet3)
                all_sprites_list.remove(bullet3)
                p3score += 5
            for star in star_hit_list:
                starsound.play()
                hitp3 = True
                bullet_list.remove(bullet3)
                all_sprites_list.remove(bullet3)
                star_obj = Star()
                star_obj.rect.x = 940
                star_obj.rect.y = 440
                starlist3.append(star_obj)
                star_sprite_list.add(starlist3)
                all_sprites_list.add(starlist3)
            for dynamite in dynamite_hit_list:
                bullet_list.remove(bullet3)
                all_sprites_list.remove(bullet3)
                p3score += 5

        if  len(floating_objects_list_bottom) < 3:
            for i in floating_objects_list_bottom:
                i.kill()
            'Load all the floating objects moving left after list is 0'
            load_ammo_object_bottom(floating_objects_list_bottom, 
                                    ammofloat_sprite_list, all_sprites_list)
            
            load_skull_bottom(floating_objects_list_bottom, 
                              skull_sprite_list, all_sprites_list)
            
            load_tnt_bottom(floating_objects_list_bottom, 
                            tnt_sprite_list, all_sprites_list)
            
            load_cow_bottom(floating_objects_list_bottom, 
                            cow_sprite_list, all_sprites_list)
            
            load_star_bottom(floating_objects_list_bottom, 
                             star_sprite_list, all_sprites_list)
            
            load_horseshoe_bottom(floating_objects_list_bottom, 
                                  horseshoe_sprite_list, all_sprites_list)
            
            load_floating_objects_bottom(floating_objects_list_bottom, 
                                         all_sprites_list)
        if len(floating_objects_list_top) < 3:
            for i in floating_objects_list_top:
                i.kill()
            'Load all the floating objects moving right after list is 0.'
            load_HorseShoe_top(floating_objects_list_top, 
                               horseshoe_sprite_list, all_sprites_list)
            
            load_AmmoObject_top(floating_objects_list_top, 
                                ammofloat_sprite_list, all_sprites_list)
            
            load_CowObject_top(floating_objects_list_top, 
                               cow_sprite_list, all_sprites_list)
            
            load_star_top(floating_objects_list_top, 
                          star_sprite_list, all_sprites_list)
            
            load_dynamite_top(floating_objects_list_top, 
                              dynamite_sprite_list, all_sprites_list)
            
            load_skull_top(floating_objects_list_top, 
                           skull_sprite_list, all_sprites_list)
            
            load_floating_objects_top(floating_objects_list_top, 
                                      all_sprites_list)
            
        move_floating_objects_top(floating_objects_list_top)
        move_floating_objects_bottom(floating_objects_list_bottom)
        
        ' Call the update() method on all the sprites'
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()
        
if __name__ == '__main__':
    main()