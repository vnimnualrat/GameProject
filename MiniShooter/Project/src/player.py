'''
Created on May 4, 2015

@author: LittleMonster
'''
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/theplayer.png')
        self.rect = self.image.get_rect()
            
    def update(self):
        """
        Gets the position of the mouse. If it's greater than 220, 
        keep it at that position until otherwise.
        """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > 220:
            self.rect.x = 220
        
        
        
            
        
    