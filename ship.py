import pygame as p
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,screen,ai_Settings):
        super().__init__()
        self.screen=screen
        self.image=p.image.load("images/ship.bmp")
        self.pix=p.transform.scale(self.image,(ai_Settings.ship_width,ai_Settings.ship_height))
        self.ai_Settings=ai_Settings
        self.rect=self.pix.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
    def blmit(self):
        self.screen.blit(self.pix,self.rect)
    def update(self):
        self.rect.centerx=self.center
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_Settings.ship_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.ai_Settings.ship_speed_factor
    def recenter_the_ship(self):
        self.center=self.screen_rect.centerx
