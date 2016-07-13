'''
Created on May 23, 2015

@author: LittleMonster
'''
import pygame
class Ammo(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/ammo.png')
        self.rect = self.image.get_rect()