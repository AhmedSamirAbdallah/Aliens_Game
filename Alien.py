import pygame as p
from pygame.sprite import Sprite
class Alines(Sprite):
    def __init__(self,screen,ai_Settings,ship):
        super().__init__()
        self.screen=screen
        self.ship=ship
        self.ai_Settings=ai_Settings
        self.image_of_alien=p.image.load("images/Alien.bmp")
        self.image=p.transform.scale(self.image_of_alien,(70,30))
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.w
        self.rect.y=self.rect.h
        self.x=float(self.rect.x)
    def check_edge(self):
        screen=self.screen.get_rect()
        if self.rect.right>=screen.right:
            return True
        if self.rect.left<=screen.left :
            return True
    def update(self):
        self.x+=(self.ai_Settings.alien_speed_factor*self.ai_Settings.direction)
        self.rect.x=self.x
