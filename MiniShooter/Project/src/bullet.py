'''
Created on May 4, 2015

@author: LittleMonster
'''
import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()

    def bulletspeed(self, y):
        'Controls the speed of the bullet'
        self.rect.y -= y
        
