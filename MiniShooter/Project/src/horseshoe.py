'''
Created on May 25, 2015

@author: LittleMonster
'''
import pygame
class HorseShoe(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/horseshoe.png')
        self.rect = self.image.get_rect()

    def moveRight(self, SCREEN):
        self.rect.x += 1
        if self.rect.x > 900:
            self.rect.x = 5
            self.rect.x += 1
          
    def moveLeft(self, SCREEN):
        self.rect.x -= 1
        if self.rect.x < 0:
            self.rect.x = 900
            self.rect.x -= 1  