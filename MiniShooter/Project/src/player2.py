'''
Created on May 24, 2015

@author: LittleMonster
'''
import pygame

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/player2.png')
        self.rect = self.image.get_rect()
 
    def moveRight(self, x):
        """
        Args: 
        x: Determines how far the player moves.
        Example:
        >>> moveLeft(1)
        moves the character left at the rate of 1.
        """
        self.rect.x += x
        if self.rect.x >= 600:
            self.rect.x = 600
        
    def moveLeft(self, x):
        """
        Args: 
        x: Determines how far the player moves.
        Example:
        >>> moveLeft(1)
        moves the character left at the rate of 1.
        """
        self.rect.x -= x
        if self.rect.x < 300:
            self.rect.x = 300
            
    